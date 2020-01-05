Simple Repo to demo deploying Scientific Python apps using conda-pack. 

This contains a simple example of how to use GitHub Actions and [conda-pack](https://conda.github.io/conda-pack/) to generate deployable assets that do not depend on conda.  This ensures that dependencies don't change under you and that the deployed environment was actually tested.  
Versioned deployable artifacts will be available from the releases page so a deploy can be reverted easily.


### Deploying the artifact:

untar/zip the OS dependent  artifcat.  The demo app will then be available under ```bin/run_example```

#### macos:
macos will complain about every single shared object within python and the related libraries (there are a lot) which is "signed" by a developer.  A solution to this is to disable GateKeeper (note this is a bad idea, so probably don't trust the macos artifacts unless they're your own).  
That said, once you run the code once you should be able to re-enable GateKeeper. 
```
sudo spctl --master-disable
spctl --status
spctl --master-enable
```
http://osxdaily.com/2015/05/04/disable-gatekeeper-command-line-mac-osx/

