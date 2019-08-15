# README

## Process

Each snake video is an AVI file.

First, videos that have a modification time that is less than 1 minute away from another video in the same file, should be seen as related and grouped together (these are found in the `all_files.txt`)

Then all of the videos must be converted to mp4 (webm does not yet have wide enough support).
`ffmpeg -i input.AVI output.mp4`

Once this has been done, a new task needs to be created for every group of videos (where a group is one or more files). In simple terms, this can be done by iterating through the `all_files.txt` and inserting each line as a task and each entry in that line as a piece of media.

The format for the media (in JSON) should be something like this:

```json
    {
        info: {
            thumb: '<thumbnail_path>'
        },
        source_id: <task_id>,
        path: <abs_path>,
        name: <name for file>,
        filetype: <mp4> //should be autodetected upon upload
    }
```

and for the task:

```json
    {
        info: {

        },
        activity_id: '09a565c4-73f8-483d-b59a-c3e5791f9a16',
        sequence: 0,
        title: <question>,
        required: true,
        allow_multiple: true
    }
```