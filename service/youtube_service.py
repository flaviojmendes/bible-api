from youtubesearchpython import VideosSearch

from config.config import MAX_VIDEO_RESULTS


class YoutubeService:

    def search_video_by_text(self, search_term):
        videos = VideosSearch(search_term, language="pt", region='BR', limit = MAX_VIDEO_RESULTS)
        return videos