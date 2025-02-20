# mp4-cutter

👉 mp4-cutter is a very simple tool for cutting videos based on a ✨special✨ text file.
> I MADE README.md BEFORE FORMAT.py, SO YOU HAVE TO WAIT.
> TODO: HOW DOES IT WORK UNDER THE HOOD.

<details>
  <summary>Why did you do that and when should I use it</summary>
  <strong>I made it, because I prefer to make long videos and add timecodes later</strong>. If you are working on a long video, you can automatically cut all the fragments into separate, small videos, then <strong>you may want to make shorts out of long video fragments</strong>, this small tool is for you! This tool will help you divide your long video into a smaller parts.
</details>
<details>
  <summary>So, how do I use it?</summary>
  First of all, <strong>you have to have <img src="https://static.cdnlogo.com/logos/f/33/ffmpeg.svg" width="36" alt="ffmpeg icon"/>`ffmpeg` and <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="24" alt="python icon"/>`python` installed and configured on your device.</strong>. Then, you need a special text file with timecodes of your video, it will tell the program how to cut your videos. Example content of `segments.txt`: `00:00 02:20 04:24 06:25 08:00`. 
  Here are some key notices for your file to work:
  <ul>
    <li>Segments have to be in format `MM:SS` or `HH:MM:SS` and separated with <b>spaces</b>.</li>
    <li>Please write zero before minutes and seconds. I don't know if it make difference to be honest, but better be safe than sorry 😇</li>
    <li>All segments need to me in ascending order, so you can't write something like: 00:20 04:20 3:20, cause video can't end before it starts.</li>
  </ul>
  > You don't need to figure out the end of the video, I took care of it, so if video has 5 minutes and your last segment is at 4 minutes mark - it will cut from 04:00 to 05:00
</details>
<details>
  <summary>What if I have time codes in different format?</summary>
  Let's say you prepared timecodes for 6 min video on youtube:
  ``` text
    00:00 intro
    02:20 what is recursion
    04:40 why should I use it
    05:50 ending
  ```
  You can do the following steps to convert it:
  <ol>
    <li>Create and open blank .txt file</li>
    <li>Paste in your raw timecdoes</li>
    <li>Open `format.py` from my repo in the same folder as .txt file</li>
    <li>Files will show. Choose your file with timestamps using keyboard numbers.</li>
    <li>Done! It should give you a file in format: "{ORIGINAL_FILE_NAME}-timecodesf.txt"</li>
  </ol>
</details>
<details>
  <summary>I have a ✨special✨ text file, now what?</summary>
  Now it it the easiest part. You just open segment.py and you find your files on the list! FFMPEG should open after choosing your ✨special✨ file with timecodes.
</details>
