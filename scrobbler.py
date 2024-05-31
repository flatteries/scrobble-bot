import pylast
import threading


API_KEY = 'ex'
API_SECRET = 'ex'
USERNAME = 'ex'
PASSWORD_HASH = pylast.md5('ex')
# rofl they didnt switch from md5 after the 2012 db leak

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=USERNAME, password_hash=PASSWORD_HASH)

def scrobble_song(artist, title, timestamp):
    network.scrobble(artist=artist, title=title, timestamp=timestamp)
    print(f"Scrobbled {title} by {artist} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}")

def scrobble_worker(artist, title, timestamps):
    for timestamp in timestamps:
        scrobble_song(artist, title, timestamp)

def main():
    artist = input("Enter the artist name: ")
    title = input("Enter the song title: ")
    count = int(input("Enter how many times to scrobble: "))
    current_time = int(time.time())
    timestamps = [current_time - (i * 123) for i in range(count)]
    num_threads = min(count, 10) 
    threads = []
    chunk_size = count // num_threads
    for i in range(num_threads):
        start_index = i * chunk_size
        if i == num_threads - 1:
            end_index = count
        else:
            end_index = start_index + chunk_size
        thread = threading.Thread(target=scrobble_worker, args=(artist, title, timestamps[start_index:end_index]))
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
