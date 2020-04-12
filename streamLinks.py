import imdb
import webbrowser

ia = imdb.IMDb()

def getStreamCode(media):
    return "tt" + str(media.movieID)

def kind(media):
    return media['kind']
    
def seasonsData(media):
    global ia
    if kind(media) != "tv series":
        return
    ia.update(media, 'episodes')
    seasons = media['episodes']
    for i in range (1,len(seasons) + 1):
        print(media["title"]+ " season " + str(i) + ": ", end="")
        season = seasons[i]
        print(str(len(season)) + " episodes")
        
def episodeData(media, season, episode):
    global ia
    season = int(season)
    episode = int(episode)
    if kind(media) != "tv series":
        return
    ia.update(media, 'episodes')
    episode = media['episodes'][season][episode]
    print(media["title"] + " season " + str(episode['season']) + " episode " + str(episode["episode"]) + ": " + episode["title"])

def genLink(title):
    global ia
    link = ""
    media = ia.search_movie(title)[0]
    mediaID = media.movieID
    if kind(media) == "tv series":
        link = genLinkTV(media)
    elif kind(media) == "movie":
        link = genLinkMovie(media)
    else: 
        return
    print(link)
    return link
    
def genLinkTV(media):
    seasonsData(media)
    a = input("\nseason: ")
    b = input("episode: ")
    print()
    episodeData(media, a, b)
    return "https://vidsrc.me/embed/" + getStreamCode(media) + "/" +  a + "-" + b + "/"
    
def genLinkMovie(media):
    print(media["title"])
    return "https://vidsrc.me/embed/" + getStreamCode(media) + "/"

while True:
    show = input("\nshow name: ")
    print()
    if show == "ext":
        break
    link = genLink(show)
    webbrowser.open(link, new=2)

input()
