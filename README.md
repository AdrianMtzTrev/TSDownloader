# Transport Stream Downloader

This python script is for downloading the files that web pages use to show media so you can watch media without annoying ads or pop-ups or being redirect to another web

## How to use it
```
python ./tsDownloader.py -u "{URL}" -n "{FileName4Output}"
```

|**Flags**| Description |
|---|---|
|-u | Url from where to iterate and fetch the TS files|
|-n | Name of output file|


## How it works
It uses a regex to find where in the url is the index number to iterate

Example URL: https://x.domain.z/a/b/c/d/seg-31-v1-a1.ts?andMaybeSmthMoreOrMaybeNot

After regex: https://x.domain.z/a/b/c/d/seg-{video}-v1-a1.ts?andMaybeSmthMoreOrMaybeNot

## TODO
| Functionality | How to use | Description | Status |
|---|---|---|---| 
| Flag | -s | index from which segment to start | In-progress | 
| Flag | -f | file to append segments | Not-started | 
| Flag | -v | verbosity | Not-started | 
| Flag | -seg | keep segments in separate files | Not-started | 
| Threads| default behavior | fetch the url with multiple threads to make download time faster | Not-started | 
