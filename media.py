import webbrowser

class Movie():
    '''定义Movie类，提供初始化函数和播放电影预告的函数'''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''
        初始化函数

        参数：
        movie_title -- 电影名称
        movie_storyline -- 电影简介
        poster_image -- 电影海报图片路径
        trailer_youtube -- 电影预告视频路径
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''播放电影预告视频'''
        webbrowser.open(self.trailer_youtube_url)
