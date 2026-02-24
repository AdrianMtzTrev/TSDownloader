# Transport Stream Downloader

This python script is for downloading the files that web pages use to show media so you can watch media without annoying ads or pop-ups or being redirect to another web

## How to use it
```
python ./tsDownloader.py -u "{URL}" -n "{FileName4Output}"
```

|**Flags**||
|---|---|
|-u | Url from where to iterate and fetch the TS files|
|-n | Name of output file|


## How it works
It uses a regex to find where in the url is the index number to iterate

Ej: https://x.domain.z/a/b/c/d/seg-31-v1-a1.ts?andMaybeSmthMoreOrMaybeNot

After regex: https://x.domain.z/a/b/c/d/seg-{video}-v1-a1.ts?andMaybeSmthMoreOrMaybeNot

## TODO
| Functionality | How to use | Description |
|---|---|---|
| Flag | -s | index segment to start|
| Flag | -f | file to append segments|
| Flag | -v | verbosity|
| Flag | -seg | keep segments in separate files|
| Threads| default behavior | fetch the url with multiple threads to make download time faster |
