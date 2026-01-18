from SoccerNet.Downloader import SoccerNetDownloader
import os

# paths
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
soccer_folder = os.path.join(desktop_path, "SoccerNetData")
os.makedirs(soccer_folder, exist_ok=True)

downloader = SoccerNetDownloader(LocalDirectory=soccer_folder)

downloader.password = ""  # replace with your NDA password

# resolution can be changed
downloader.downloadGames(
    files=["1_720p.mkv", "2_720p.mkv"],
    split=["train"]  # only train , we can do val and test also
)

print("Download started! Check your folder:", soccer_folder)
