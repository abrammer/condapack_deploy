Simple Repo to demo deploying Scientific Python apps using conda-pack. 

We'll utilise GitHub actions to build and artifact the conda environment. 


###Deploying the artifact:

untar/zip the OS dependent  artifcat.  The demo app will then be available under ```bin/run_example```

####macos:
macos will complain about every single shared object within python and related libraries (there are a lot).  A solution to this is to disable GateKeeper (note this is a bad idea, so probably don't trust the artifacts unless they're your own).  
That said, once you run the code once you should be able to re-enable GateKeeper. 
```
sudo spctl --master-disable
spctl --status
spctl --master-enable
```
http://osxdaily.com/2015/05/04/disable-gatekeeper-command-line-mac-osx/


