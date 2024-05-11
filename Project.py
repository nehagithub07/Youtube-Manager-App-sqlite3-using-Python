import sqlite3
conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
             id INTEGER PRIMARY KEY, 
             name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def  add_videos(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?, ?)", (name, time))
    conn.commit() #value insert hogyi

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))   # single value jb dete hai to coma "," lgana pdta hai fr ye tuple me chla jata h
    conn.commit()


def main():
    while True:
        print("\n Youtube Managar || Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos details")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        choice = input("Enter Your Choice: ")
        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter video time: ")
                add_videos(name, time)
            case '3':
                video_id = input("Enter the video id: ")
                name = input("Enter the video name: ")
                time = input("Enter video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video id: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice")
    conn.close() # isliye kia hai hmara database currpt na ho jaye



if __name__ == "__main__":
    main()

