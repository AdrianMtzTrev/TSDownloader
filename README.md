# Transport Stream Downloader

This python script is for downloading the files that web pages use to show media so you can watch media without annoying ads or pop-ups or being redirect to another web

## How to use it

**Flags**
-u = Url from where to iterate and fetch the TS files
-n = Name of output file

TODO:
-s = index segment to start
-f = file to append segments
-v = verbosity
-seg = keep segments in separate files
Threads

## How it works
It uses a regex to find where in the url is the index number to iterate

		 Number to iterate ⬇
Ej: https://x.domain.z/a/b/c/d/seg-31-v1-a1.ts?andMaybeSmthMoreOrMaybeNot
After regex: https://x.domain.z/a/b/c/d/seg-{video}-v1-a1.ts?andMaybeSmthMoreOrMaybeNot

