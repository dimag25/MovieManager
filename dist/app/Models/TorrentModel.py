class TorrentModel():
    def __init__(self, torrentDict, title):
        self.title = title
        self.quality = torrentDict["quality"]
        self.torrent_peers = torrentDict["torrent_peers"]
        self.torrent_seeds = torrentDict["torrent_seeds"]
        self.torrent_url = self.createTorrentURL(torrentDict["torrent_url"])

    @staticmethod
    def createTorrentURL(url):
        return "<a href={0}>{1}</a>".format(url, url)
