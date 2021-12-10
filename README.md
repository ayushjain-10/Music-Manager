# FlaskMusicManagement


## Installation 
- Make a python virtual environment
- run `pip install -r requirements.txt`
- run `flask run`
- Go to `http://127.0.0.1:5000/`


DB is present with few songs 


Your task is to create a music management/sharing/streaming platform. A user should be able to upload/download/play/delete/search songs. All songs go into a common playlist (which shows up when the user wants to view all songs).

Detailed requirements: 
- Upload a songo 
    1. Has metadata fields title, artist, album
    2. Song should have a unique URL which can be shared with anyone publically.
- Delete an uploaded song
- View all songs
- Search for any song via album/title/artist
- Stream song
- Each song should have a page where you can play the song from the browser itself. 
    1. Use HTML5 for this, not flash.
    2. Clicking on the unique URL of a song should lead to this page.
    3. Clicking on a song entity from either search or view all pages should also lead to this page.
    4. There should be an option to download this song



