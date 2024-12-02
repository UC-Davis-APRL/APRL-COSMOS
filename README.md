# APRL-COSMOS Plugin

This plugin configures OpenC3 for use with APRL firmware.

See the [OpenC3](https://docs.openc3.com) documentation for all things OpenC3.

## Getting Started

1. Edit the .gemspec file fields: name, summary, description, authors, email, and homepage
2. Update the LICENSE.txt file with yo~~ur company~~ mamas name

## Building non-tool / widget plugins

1. Install your dependencies
   - Python
2. Add openc3.sh to your PATH
   - EXPORT PATH="$PATH:/path/to/cosmos-project" (Temporary)
   - Add the above line to ~/.bashrc (Permanent)
3. `openc3.sh cli rake build VERSION=X.Y.Z`
   - The plugin will be named APRL-COSMOS-X.Y.Z.gem
   - Install the gem into COSMOS to set it up

## Building tool / widget plugins using a local Ruby/Node/Yarn/Rake Environment

1. yarn
1. rake build VERSION=1.0.0

## Building tool / widget plugins using Docker and the openc3-node container

If you don’t have a local node environment, you can use our openc3-node container to build custom tools and custom widgets

Mac / Linux:

```
docker run -it -v `pwd`:/openc3/local:z -w /openc3/local docker.io/openc3inc/openc3-node sh
```

Windows:

```
docker run -it -v %cd%:/openc3/local -w /openc3/local docker.io/openc3inc/openc3-node sh
```

1. yarn
1. rake build VERSION=1.0.0

## Installing into OpenC3 COSMOS

### PREREQ
1. Ensure that ```OPENC3_DEMO=1``` is commented out in the .env file
2. Ensure that UDP port 1682 and another required ports are exposed on the docker in the ```openc3-operator:``` section of the compose.yaml 
   ```
   ports:
      - "127.0.0.1:1682:1682/udp" # etc etc
   ```

### Installing Plugin
1. Go to the OpenC3 Admin Tool, Plugins Tab
2. Click the paperclip icon and choose your plugin.gem file
3. Fill out plugin parameters
4. Click Install


## Contributing

Contact Jason `(@nuclearfizzler)`, or the relevant Electrical team member for how to contribute.

## License

This OpenC3 plugin is released under the MIT License. See [LICENSE.txt](LICENSE.txt)
