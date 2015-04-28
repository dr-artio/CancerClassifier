module Handler.Home where

import Import
import Yesod.Form.Bootstrap3 (BootstrapFormLayout (..), renderBootstrap3,
                              withSmallInput)
import qualified Data.Text as T
import qualified Data.Conduit.List as CL
import Data.Conduit
import Data.Conduit.Binary
import Data.Default
import Yesod
import Yesod.Default.Util
import Control.Monad.Trans.Resource (runResourceT)
import Network.Socket.ByteString
import Network.Socket
import Network.Socket.SendFile
import qualified Data.List as L
import qualified Data.ByteString as B
import qualified Data.ByteString.Lazy.Char8 as BS
import qualified Data.ByteString.Char8 as C
import Data.ByteString.Internal (unpackBytes)
import Data.Time (getCurrentTime)
import Codec.Archive.Tar (create)
import qualified System.IO as SI
-- This is a handler function for the GET request method on the HomeR
-- resource pattern. All of your resource patterns are defined in
-- config/routes
--
-- The majority of the code you will write in Yesod lives in these handler
-- functions. You can spread them across multiple files if you are so
-- inclined, or create a single monolithic file.


getFileName :: Maybe (FileInfo, Text) -> FileInfo
getFileName submission = case submission of
                        Just igor -> fst igor


getEmail :: Maybe (FileInfo, Text) -> Text
getEmail submission = case submission of
                        Just igor -> snd igor
                        otherwise -> "Vafli v rotik"


filterNewLine :: Word8 -> Bool
filterNewLine character = character /= 10



sendData :: String -> IO String
sendData file = withSocketsDo $ do
    sock <- socket AF_INET Stream defaultProtocol
    addr <- inet_addr "131.96.155.200"
    Network.Socket.connect sock (SockAddrInet 8080 addr)
    Network.Socket.SendFile.sendFile sock file
    Network.Socket.recv sock 1024



getHomeR :: Handler Html
getHomeR = do
    (formWidget, formEnctype) <- generateFormPost sampleForm
    let submission = Nothing :: Maybe (FileInfo, Text)
        handlerName = "getHomeR" :: Text
        user_email = "MMMMMMMM" :: Text
        upload_date = "MMMMMMMMMM" :: Text
        upload_file = "MMMMMMMMMMM" :: Text
        predi = "MMMMMMMMMM" :: Text
       
    defaultLayout $ do
        aDomId <- newIdent
        setTitle "Classifying Cancer"
        $(widgetFile "homepage")

postHomeR :: Handler Html
postHomeR = do
    ((result, formWidget), formEnctype) <- runFormPost sampleForm
    let handlerName = "postHomeR" :: Text
        submission = case result of
            FormSuccess res -> Just res
            _ -> Nothing

    curTime <- liftIO $ getCurrentTime
    let email = getEmail submission
        fi = getFileName submission
        newFileName = concat [T.unpack email, "___", show curTime, "___", T.unpack $ fileName fi]
        myName = "meta___" ++ T.unpack email ++ "___" ++ show curTime ++ ".txt"
        tarName = concat ["/tmp/", T.unpack email, "___", show curTime, ".tar"]
    _ <- liftIO $ SI.writeFile ("/tmp/" ++ myName) ((T.unpack email) ++ "__" ++ (show curTime) ++ "__" ++ (T.unpack $ fileName fi))
    _ <- liftIO $ fileMove fi ("/tmp/" ++ newFileName)
    _ <- liftIO $ create tarName "/tmp" [newFileName, myName]
    message <- liftIO $ sendData tarName

    let ws = words message
        user_email = T.pack (ws L.!! 1)
        upload_date = T.pack ((ws L.!! 2) ++ " " ++ (ws L.!! 3) ++ " " ++ (ws L.!! 4))
        upload_file = T.pack (L.last ws)
        predi = T.pack (L.head ws)

    defaultLayout $ do
        aDomId <- newIdent
        setTitle "Classifying Cancer"
        $(widgetFile "homepage")

sampleForm :: Form (FileInfo, Text)
sampleForm = renderBootstrap3 BootstrapBasicForm $ (,)
    <$> fileAFormReq "Choose a file"
    <*> areq emailField (withSmallInput "Your e-mail address\t") Nothing
