Migrating ES and kibana to podman from Docker desktop.

How to use podman

Run podman help in the terminal for a list of commands to interact with Podman. For example, try the 'Create' button within the Containers tab of Podman Desktop and view your containers with podman:

$ podman ps


How to use kubectl

Run kubectl help in the terminal for a list of commands to interact with your Kubernetes cluster. For example, try the 'Deploy to Kubernetes' button within Podman Desktop and view your pods with kubectl:

$ kubectl get pods



How to use Compose
Run podman compose up (podman CLI v4.7.0+) or docker-compose in a directory with a compose.yaml. Podman Desktop will automatically detect the Compose deployment and show it in the container list.'

$ podman compose up



To import a Docker image into Podman, the recommended method is to use the podman pull command with the docker-daemon transport, which copies the image directly from the Docker daemon's storage into Podman's storage. Alternatively, you can use the docker save and podman load commands. 
Method 1: Direct Copy (Recommended)
This method uses Podman to pull images directly from the running Docker daemon's internal storage. 
List Docker images with the correct format for Podman to use:
bash

docker images --format 'docker-daemon:{{.Repository}}:{{.Tag}}' | grep -v '<none>'

docker images --format 'docker:{{.Repository}}:{{.Tag}}' | grep -v '<none>'



This command outputs a list of image references that Podman can understand, while filtering out intermediate or untagged images.
Pipe the list to podman pull:
bash

docker images --format 'docker-daemon:{{.Repository}}:{{.Tag}}' | grep -v '<none>' | xargs podman pull

docker images --format 'docker://{{.Repository}}:{{.Tag}}' | grep -v '<none>' | xargs podman pull




xargs executes the podman pull command for each image reference in the list, effectively copying them into Podman's local storage.
Verify the images in Podman:
bash
podman images
 
Method 2: Save and Load Archive (Alternative)
This approach involves exporting the Docker image to a tarball and then loading that tarball into Podman. 
Save the Docker image to a tar archive:
bash
docker save <image_name>:<tag> > <image_archive_name>.tar
This command saves the image and its parent layers to a single archive file.

Load the image from the tar archive into Podman:

bash

podman load -i <image_archive_name>.tar

The podman load command is specifically used for importing archives created by docker save or podman save.

Verify the image in Podman:

bash

podman images
 
Note on podman import: The podman import command is used for importing a container's filesystem from a tarball created by podman export or docker export. It saves the tarball as a new image but does not preserve configuration like ENTRYPOINT or CMD instructions, making podman load the correct choice for full image archives. 



Error: unsupported transport docker-daemon; only docker transport is supported

AI Overview
The error "unsupported transport docker-daemon; only docker transport is supported" typically occurs when using tools like Podman or Skopeo on remote clients (such as macOS or Windows without WSL2), where the docker-daemon: transport is not supported. 
Cause of the Error
This error message indicates that:
You are likely using a container management tool (like Podman) that supports multiple image "transports" (ways to specify the image source, e.g., docker://, dir:, oci-archive:).
On certain operating systems or configurations (especially remote clients), the ability to access the local Docker daemon's internal storage via docker-daemon: is explicitly disabled or not implemented. The tool is telling you to use the standard docker:// transport instead, which pulls images from a container registry (like Docker Hub). 
How to Fix the Error
The solution depends on the command you were trying to run:
Change the transport in your command: Modify the image reference in your command from docker-daemon:<image_name> to docker://<image_name>.Example:
Instead of: podman pull docker-daemon:myimage:latest

Use: podman pull docker://myimage:latest

Ensure the Docker daemon is running: If the tool is trying to connect to a local Docker daemon (even if the transport is the issue), make sure the Docker daemon service is running on your system. You may need to restart the Docker application.
Check Podman documentation: If you are using Podman, review the Podman documentation for specific guidance on supported transports for your environment. On remote machines, docker:// is the only supported transport for pulling images from a registry.
Use the correct context/socket: Ensure that your container client is pointing to the correct Docker socket if you have multiple setups (e.g., Docker Desktop and Podman). 


Last login: Thu Dec 25 17:22:45 on ttys003
Server:		100.64.0.2
Address:	100.64.0.2#53

Non-authoritative answer:
Name:	dynamodb.us-east-1.amazonaws.com
Address: 3.218.181.105

Matching Java Virtual Machines (1):
    21.0.8 (arm64) "Oracle Corporation" - "Java SE 21.0.8" /Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home
/Users/blauerbock/workspaces/python-workout/logging/logging_package/logapp:
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
% which podman
/opt/podman/bin/podman
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
% docker images --format 'docker-daemon:{{.Repository}}:{{.Tag}}' | grep -v '<none>'
docker-daemon:ai-powered-search-notebooks:latest
docker-daemon:ai-powered-search-solr:latest
docker-daemon:docker.elastic.co/elasticsearch/elasticsearch:9.2.1-arm64
docker-daemon:docker.elastic.co/elasticsearch/elasticsearch:9.2.1
docker-daemon:docker.elastic.co/kibana/kibana:9.2.1-arm64
docker-daemon:docker.elastic.co/kibana/kibana:9.2.1
docker-daemon:shellserver2-app:latest
docker-daemon:local/r8-systemd-httpd:latest
docker-daemon:local/r8-systemd:latest
docker-daemon:fedora:latest
docker-daemon:alpine:latest
docker-daemon:nginx:latest
docker-daemon:ubuntu:latest
docker-daemon:zookeeper:3.5.8
docker-daemon:kodekloud/simple-webapp:latest
docker-daemon:kodekloud/webapp:latest
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
% docker images --format 'docker-daemon:{{.Repository}}:{{.Tag}}' | grep -v '<none>' | xargs podman pull
Error: unsupported transport docker-daemon in "docker-daemon:ai-powered-search-notebooks:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:ai-powered-search-solr:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:docker.elastic.co/elasticsearch/elasticsearch:9.2.1-arm64": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:docker.elastic.co/elasticsearch/elasticsearch:9.2.1": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:docker.elastic.co/kibana/kibana:9.2.1-arm64": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:docker.elastic.co/kibana/kibana:9.2.1": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:shellserver2-app:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:local/r8-systemd-httpd:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:local/r8-systemd:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:fedora:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:alpine:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:nginx:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:ubuntu:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:zookeeper:3.5.8": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:kodekloud/simple-webapp:latest": only docker transport is supported
Error: unsupported transport docker-daemon in "docker-daemon:kodekloud/webapp:latest": only docker transport is supported
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
% docker images --format 'docker:{{.Repository}}:{{.Tag}}' | grep -v '<none>'

docker:ai-powered-search-notebooks:latest
docker:ai-powered-search-solr:latest
docker:docker.elastic.co/elasticsearch/elasticsearch:9.2.1-arm64
docker:docker.elastic.co/elasticsearch/elasticsearch:9.2.1
docker:docker.elastic.co/kibana/kibana:9.2.1-arm64
docker:docker.elastic.co/kibana/kibana:9.2.1
docker:shellserver2-app:latest
docker:local/r8-systemd-httpd:latest
docker:local/r8-systemd:latest
docker:fedora:latest
docker:alpine:latest
docker:nginx:latest
docker:ubuntu:latest
docker:zookeeper:3.5.8
docker:kodekloud/simple-webapp:latest
docker:kodekloud/webapp:latest
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
% docker images --format 'docker:{{.Repository}}:{{.Tag}}' | grep -v '<none>' | xargs podman pull
Error: parsing reference "docker:ai-powered-search-notebooks:latest": invalid reference format
Error: parsing reference "docker:ai-powered-search-solr:latest": invalid reference format
Error: parsing reference "docker:docker.elastic.co/elasticsearch/elasticsearch:9.2.1-arm64": invalid reference format
Error: parsing reference "docker:docker.elastic.co/elasticsearch/elasticsearch:9.2.1": invalid reference format
Error: parsing reference "docker:docker.elastic.co/kibana/kibana:9.2.1-arm64": invalid reference format
Error: parsing reference "docker:docker.elastic.co/kibana/kibana:9.2.1": invalid reference format
Error: parsing reference "docker:shellserver2-app:latest": invalid reference format
Error: parsing reference "docker:local/r8-systemd-httpd:latest": invalid reference format
Error: parsing reference "docker:local/r8-systemd:latest": invalid reference format
Error: parsing reference "docker:fedora:latest": invalid reference format
Error: parsing reference "docker:alpine:latest": invalid reference format
Error: parsing reference "docker:nginx:latest": invalid reference format
Error: parsing reference "docker:ubuntu:latest": invalid reference format
Error: parsing reference "docker:zookeeper:3.5.8": invalid reference format
Error: parsing reference "docker:kodekloud/simple-webapp:latest": invalid reference format
Error: parsing reference "docker:kodekloud/webapp:latest": invalid reference format
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
% docker images --format 'docker//:{{.Repository}}:{{.Tag}}' | grep -v '<none>' | xargs podman pull
Error: parsing reference "docker//:ai-powered-search-notebooks:latest": invalid reference format
Error: parsing reference "docker//:ai-powered-search-solr:latest": invalid reference format
Error: parsing reference "docker//:docker.elastic.co/elasticsearch/elasticsearch:9.2.1-arm64": invalid reference format
Error: parsing reference "docker//:docker.elastic.co/elasticsearch/elasticsearch:9.2.1": invalid reference format
Error: parsing reference "docker//:docker.elastic.co/kibana/kibana:9.2.1-arm64": invalid reference format
Error: parsing reference "docker//:docker.elastic.co/kibana/kibana:9.2.1": invalid reference format
Error: parsing reference "docker//:shellserver2-app:latest": invalid reference format
Error: parsing reference "docker//:local/r8-systemd-httpd:latest": invalid reference format
Error: parsing reference "docker//:local/r8-systemd:latest": invalid reference format
Error: parsing reference "docker//:fedora:latest": invalid reference format
Error: parsing reference "docker//:alpine:latest": invalid reference format
Error: parsing reference "docker//:nginx:latest": invalid reference format
Error: parsing reference "docker//:ubuntu:latest": invalid reference format
Error: parsing reference "docker//:zookeeper:3.5.8": invalid reference format
Error: parsing reference "docker//:kodekloud/simple-webapp:latest": invalid reference format
Error: parsing reference "docker//:kodekloud/webapp:latest": invalid reference format
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
% docker images --format 'docker://{{.Repository}}:{{.Tag}}' | grep -v '<none>' | xargs podman pull

Trying to pull docker.io/library/ai-powered-search-notebooks:latest...
Trying to pull docker.io/library/ai-powered-search-solr:latest...
Trying to pull docker.elastic.co/elasticsearch/elasticsearch:9.2.1-arm64...
Getting image source signatures
Copying blob sha256:0c2731bbe27c69a9b9cf6b20f81e84f7ec0bd7d3766d0aa35780fcb3f5d6f37e
Copying blob sha256:654413581a8c7f2858d580205f799d054cc63ae39901e2742e7063203f2fe909
Copying blob sha256:5445572ec3529960bfc7220eb17a3ce2d0d052d8099e053978becd70d9e9a36f
Copying blob sha256:bc26c094cf0742184f08c89cca800e5c1e7e85af75d1c69cb4318f854d14a8b5
Copying blob sha256:b5498d43622ce9413ee7a8ffacf343ef5914b6e9a35fe5cc35f3d2c97baabbde
Copying blob sha256:4ca545ee6d5db5c1170386eeb39b2ffe3bd46e5d4a73a9acbebc805f19607eb3
Copying blob sha256:3bcc812bd9b77256f44ba7cd3c44b29c4dd4d1e7e725f0c6703b0a44055ac704
Copying blob sha256:2f7a46f4f991898d4f54289b4e15b6d714da6c2d9de32c8ac62173882c1c75e2
Copying blob sha256:8cdc5fb60f3c67a5c6163da65c30e7a1204b5617b8f3d40258a92f0bff3bf329
Copying blob sha256:a0b70c51cab0fd738596ffe7e7a7b1d5b1b2daf03f95a1ca419d82da77c4ee75
Copying config sha256:541fb6dbb0d5d3283003dbc40728c634524efb604556db4a392a82c4b031477a
Writing manifest to image destination
541fb6dbb0d5d3283003dbc40728c634524efb604556db4a392a82c4b031477a
Trying to pull docker.elastic.co/elasticsearch/elasticsearch:9.2.1...
Getting image source signatures
Copying blob sha256:0c2731bbe27c69a9b9cf6b20f81e84f7ec0bd7d3766d0aa35780fcb3f5d6f37e
Copying blob sha256:654413581a8c7f2858d580205f799d054cc63ae39901e2742e7063203f2fe909
Copying blob sha256:b5498d43622ce9413ee7a8ffacf343ef5914b6e9a35fe5cc35f3d2c97baabbde
Copying blob sha256:bc26c094cf0742184f08c89cca800e5c1e7e85af75d1c69cb4318f854d14a8b5
Copying blob sha256:4ca545ee6d5db5c1170386eeb39b2ffe3bd46e5d4a73a9acbebc805f19607eb3
Copying blob sha256:5445572ec3529960bfc7220eb17a3ce2d0d052d8099e053978becd70d9e9a36f
Copying blob sha256:3bcc812bd9b77256f44ba7cd3c44b29c4dd4d1e7e725f0c6703b0a44055ac704
Copying blob sha256:2f7a46f4f991898d4f54289b4e15b6d714da6c2d9de32c8ac62173882c1c75e2
Copying blob sha256:8cdc5fb60f3c67a5c6163da65c30e7a1204b5617b8f3d40258a92f0bff3bf329
Copying blob sha256:a0b70c51cab0fd738596ffe7e7a7b1d5b1b2daf03f95a1ca419d82da77c4ee75
Copying config sha256:541fb6dbb0d5d3283003dbc40728c634524efb604556db4a392a82c4b031477a
Writing manifest to image destination
541fb6dbb0d5d3283003dbc40728c634524efb604556db4a392a82c4b031477a
Trying to pull docker.elastic.co/kibana/kibana:9.2.1-arm64...
Getting image source signatures
Copying blob sha256:54ae3ebe88a517ae9f1d48f35a4f11dd2e6fb8b4f85d36b6b809718b28b72214
Copying blob sha256:c674dc6e7d832c5744f20f34be8a210129a423fd0936f95e112c6eed20863a44
Copying blob sha256:5445572ec3529960bfc7220eb17a3ce2d0d052d8099e053978becd70d9e9a36f
Copying blob sha256:253a00c1cf6de41afb7bde4b9e25a45f9f1d6e4d7b15f8e97f1f082be1e7ed21
Copying blob sha256:dfabe7e82fe67ff9b622d8a505665239dacbc3a0bcf67eee4189685086c500c5
Copying blob sha256:37d604bd56aa96f3b41a1f4208e6161241827e13f36e2c67fc26573ac192130a
Copying blob sha256:4ca545ee6d5db5c1170386eeb39b2ffe3bd46e5d4a73a9acbebc805f19607eb3
Copying blob sha256:d6d9bcabbf26c6ad05c65d6df0adec57e2f85f05a17a9b1752ae34de36c407c8
Copying blob sha256:a892afde0dfbe0326bd82bb6bd2c2c8f7acca6cd56c6a3c02605a4e064ca93e3
Copying blob sha256:749ad5230fea69a5855982691fc0e940d0db1888316e5bb9e1da9b723447971a
Copying blob sha256:86f103467d31e2f3fbd525986889bc38534c79a481cfb56851823a6d72943a09
Copying blob sha256:afe4e6af92735c8ff7d568b539a754053f8414a45aac9e0cec2e6068ad852c23
Copying blob sha256:746320928895149a7924ca7638a7fcbcc149189e1c711870c457aab9e2fd726f
Copying blob sha256:a0dc7c13824616fb4428881a125d4d515fca8d48b9590742b54e5e50ee76ce9d
Copying config sha256:78bc3ce9b54249beef8e84934fed1b60158ca99e0b6bafb317ade6fd0bff3747
Writing manifest to image destination
78bc3ce9b54249beef8e84934fed1b60158ca99e0b6bafb317ade6fd0bff3747
Trying to pull docker.elastic.co/kibana/kibana:9.2.1...
Getting image source signatures
Copying blob sha256:54ae3ebe88a517ae9f1d48f35a4f11dd2e6fb8b4f85d36b6b809718b28b72214
Copying blob sha256:c674dc6e7d832c5744f20f34be8a210129a423fd0936f95e112c6eed20863a44
Copying blob sha256:5445572ec3529960bfc7220eb17a3ce2d0d052d8099e053978becd70d9e9a36f
Copying blob sha256:253a00c1cf6de41afb7bde4b9e25a45f9f1d6e4d7b15f8e97f1f082be1e7ed21
Copying blob sha256:4ca545ee6d5db5c1170386eeb39b2ffe3bd46e5d4a73a9acbebc805f19607eb3
Copying blob sha256:dfabe7e82fe67ff9b622d8a505665239dacbc3a0bcf67eee4189685086c500c5
Copying blob sha256:d6d9bcabbf26c6ad05c65d6df0adec57e2f85f05a17a9b1752ae34de36c407c8
Copying blob sha256:37d604bd56aa96f3b41a1f4208e6161241827e13f36e2c67fc26573ac192130a
Copying blob sha256:a892afde0dfbe0326bd82bb6bd2c2c8f7acca6cd56c6a3c02605a4e064ca93e3
Copying blob sha256:749ad5230fea69a5855982691fc0e940d0db1888316e5bb9e1da9b723447971a
Copying blob sha256:86f103467d31e2f3fbd525986889bc38534c79a481cfb56851823a6d72943a09
Copying blob sha256:afe4e6af92735c8ff7d568b539a754053f8414a45aac9e0cec2e6068ad852c23
Copying blob sha256:746320928895149a7924ca7638a7fcbcc149189e1c711870c457aab9e2fd726f
Copying blob sha256:a0dc7c13824616fb4428881a125d4d515fca8d48b9590742b54e5e50ee76ce9d
Copying config sha256:78bc3ce9b54249beef8e84934fed1b60158ca99e0b6bafb317ade6fd0bff3747
Writing manifest to image destination
78bc3ce9b54249beef8e84934fed1b60158ca99e0b6bafb317ade6fd0bff3747
Trying to pull docker.io/library/shellserver2-app:latest...
Trying to pull docker.io/local/r8-systemd-httpd:latest...
Trying to pull docker.io/local/r8-systemd:latest...
Trying to pull docker.io/library/fedora:latest...
Getting image source signatures
Copying blob sha256:9a97681a321eff20d482f7f13cb9f355e41b33a70c67b16314080586f8b600f6
Copying config sha256:e108db52fd27a69f573f2dc5f754399239116721126d27f67345f145352af8a6
Writing manifest to image destination
e108db52fd27a69f573f2dc5f754399239116721126d27f67345f145352af8a6
Trying to pull docker.io/library/alpine:latest...
Getting image source signatures
Copying blob sha256:f6b4fb9446345fcad2db26eac181fef6c0a919c8a4fcccd3bea5deb7f6dff67e
Copying config sha256:e8f9ca9f1870bc194d961e259fd1340c641bf188e0d02e58b86b86445a4bc128
Writing manifest to image destination
e8f9ca9f1870bc194d961e259fd1340c641bf188e0d02e58b86b86445a4bc128
Trying to pull docker.io/library/nginx:latest...
Getting image source signatures
Copying blob sha256:fda1d961e2b70f435ee701baaa260a569d7ea2eacd9f6dba8ac0320dc9b7d9fe
Copying blob sha256:89d0a1112522e6e01ed53f0b339cb1a121ea7e19cfebdb325763bf5045ba7a47
Copying blob sha256:f626fba1463b32b20f78d29b52dcf15be927dbb5372a9ba6a5f97aad47ae220b
Copying blob sha256:1b7c70849006971147c73371c868b789998c7220ba42e777d2d7e5894ac26e54
Copying blob sha256:b8b0307e95c93307d99d02d3bdc61c3ed0b8d26685bb9bafc6c62d4170a2363e
Copying blob sha256:fe1d23b41cb3b150a19a697809a56f455f1dac2bf8b60c8a1d0427965126aaf9
Copying blob sha256:10dbff0ec650f05c6cdcb80c2e7cc93db11c265b775a7a54e1dd48e4cbcebbbc
Copying config sha256:de437b5614ad7ef640175c1204414667adecd421752f7ddf3388edd063403a6e
Writing manifest to image destination
de437b5614ad7ef640175c1204414667adecd421752f7ddf3388edd063403a6e
Trying to pull docker.io/library/ubuntu:latest...
Getting image source signatures
Copying blob sha256:97dd3f0ce510a30a2868ff104e9ff286ffc0ef01284aebe383ea81e85e26a415
Copying config sha256:9a84ec2d5dd7ad691e3df0d6e7c6e7ebd6ba67fdd1b6172588c009c12359d307
Writing manifest to image destination
9a84ec2d5dd7ad691e3df0d6e7c6e7ebd6ba67fdd1b6172588c009c12359d307
Trying to pull docker.io/library/zookeeper:3.5.8...
Getting image source signatures
Copying blob sha256:5f650b749d4cbcc61bd57ab0562e36351df0eaccbd8225fd81eb6442bfab7b95
Copying blob sha256:96062c0c15f683e4abb09efb938dfd7ff23002f72a375c75492d44bde3a6c26f
Copying blob sha256:e679cf9f2bb808fcddbdc7e9d65f3fd776d4f4173dabdd4683340d1b5f0d02fb
Copying blob sha256:6b6f368489861719a20fe5326b5f5178ca41f1f618ffcbd80f72f75bce9236f6
Copying blob sha256:73a69e47b8eb07345ad24896d87c049023f42988f58da6c0f9e6b5b63614468f
Copying blob sha256:83c5cfdaa5385ea6fc4d31e724fd4dc5d74de847a7bdd968555b8f2c558dac0e
Copying blob sha256:89d6b14429539104f0badeac05543b65cfc1c45f968d8a70f409d54dd9b9dcd3
Copying blob sha256:fd868a48b5f2048fefe19e2ef59c3712cfd626fcc37c8f092425545ce3d4ece7
Copying config sha256:ff22fb864fe6763b9337e262c5d40c70c6f7e75fd64bb63622b0ee6e615b1d9d
Writing manifest to image destination
ff22fb864fe6763b9337e262c5d40c70c6f7e75fd64bb63622b0ee6e615b1d9d
Trying to pull docker.io/kodekloud/simple-webapp:latest...
Getting image source signatures
Copying blob sha256:4fe2ade4980c2dda4fc95858ebb981489baec8c1e4bd282ab1c3560be8ff9bde
Copying blob sha256:7454877e71d02105302272ad3939c016553f493fbb374082ec11e34e3ddad5b8
Copying blob sha256:7cf6a1d62200b34e1e616cee74d0b8d3f2c2a09da9db5f1e221f23dc457b09fa
Copying blob sha256:f0d690b9e4959a736826b4a9cfb9d4e40517e4813e985708d7e8e323115dd0da
Copying blob sha256:fac5d45ad062a27ac3b53bc615c47f7972e97600f55db85dc02f7c5b2af61ac9
Copying blob sha256:dd9b067ef6fd92b84a2582ff5a0b83edefd54b04bb5dbdba98a3d705a8e2148b
Copying blob sha256:e337be014a61dde923da688e3f8d6d7dc4a886aafe4cefbbd69a76825d7748ca
Copying config sha256:c6e3cd9aae3645a98dd69c15b048614603efce6cda26c60f5f7e867ef68f729f
Writing manifest to image destination
WARNING: image platform (linux/amd64) does not match the expected platform (linux/arm64)
c6e3cd9aae3645a98dd69c15b048614603efce6cda26c60f5f7e867ef68f729f
Trying to pull docker.io/kodekloud/webapp:latest...
Getting image source signatures
Copying blob sha256:dd2f6ec7cee45b0ccfd2d578bf55299316cd6d648ca55edf5011c3e76e242d0b
Copying blob sha256:f7d512d8250289b154a8e982ff1272ed1376e407bf21f314cd55627c22e5598e
Copying blob sha256:60730f9603637b2b4d71f56eca6b7cf26f3c3a59478c45f1e53733901ea89b02
Copying blob sha256:25bb6f291ceb2dcdd3e24aa3a00ef625e6e1a022779283fc2c1b2ccecbc0d162
Copying blob sha256:a7cad26d035791e5bf04d6479b03dee59d40a504cfd0b54840966f98b39abfc4
Copying blob sha256:630ceed02486a128742ac2b5c3105c88ad28f410a0b2e08ff4ddae2878483924
Copying blob sha256:c24bc06e3fe8e274a8aa1ade8119f362e2eeb8a4a5e0f29bec71f1f40789a3c2
Copying blob sha256:dd9871015947dbe6168d465839e486b02d354d506d5c47afcdede5cc22c4909b
Copying config sha256:1a45ba829f10d32685d9e1a932c6f95089840d870117768b67d496b276fc33dd
Writing manifest to image destination
WARNING: image platform (linux/amd64) does not match the expected platform (linux/arm64)
1a45ba829f10d32685d9e1a932c6f95089840d870117768b67d496b276fc33dd
Error: unable to copy from source docker://ai-powered-search-notebooks:latest: initializing source docker://ai-powered-search-notebooks:latest: reading manifest latest in docker.io/library/ai-powered-search-notebooks: requested access to the resource is denied
Error: unable to copy from source docker://ai-powered-search-solr:latest: initializing source docker://ai-powered-search-solr:latest: reading manifest latest in docker.io/library/ai-powered-search-solr: requested access to the resource is denied
Error: unable to copy from source docker://shellserver2-app:latest: initializing source docker://shellserver2-app:latest: reading manifest latest in docker.io/library/shellserver2-app: requested access to the resource is denied
Error: unable to copy from source docker://local/r8-systemd-httpd:latest: initializing source docker://local/r8-systemd-httpd:latest: reading manifest latest in docker.io/local/r8-systemd-httpd: requested access to the resource is denied
Error: unable to copy from source docker://local/r8-systemd:latest: initializing source docker://local/r8-systemd:latest: reading manifest latest in docker.io/local/r8-systemd: requested access to the resource is denied
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock
%


Migrated ES-arm64 to podman.  Started ES

The enrollment token is automatically generated when you start Elasticsearch for the first time. You might need to scroll back a bit in the terminal to view it.

To generate a new enrollment token, run the following command from the Elasticsearch installation directory:

✄𐘗bash code block:✄𐘗
bin/elasticsearch-create-enrollment-token --scope kibana


In podman ES terminal:

[elasticsearch@f005f1289400 ~]$ bin/elasticsearch-create-enrollment-token --scope kibana

WARNING: Owner of file [/usr/share/elasticsearch/config/users] used to be [root], but now is [elasticsearch]
WARNING: Owner of file [/usr/share/elasticsearch/config/users_roles] used to be [root], but now is [elasticsearch]
eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTAuODguMC4yOjkyMDAiXSwiZmdyIjoiZjY1NzRiNmU5ZjFlODMwY2YyN2FkNWMxNTU3NzAwZjFlZjVmZmMyYjZiZjU1MDMyOGU0NDU0YzE4MGU4NmU4MiIsImtleSI6Im9INWJZSnNCeWpJb3JadXAzZ0hDOkxGVWI0MDIxYkV4aG5DbHVGWUg4N1EifQ==
[elasticsearch@f005f1289400 ~]$ 


Verification required

Copy the code from the Kibana server or run (in podman kibana terminal):

bin/kibana-verification-code 

to retrieve it.


Password for the [elastic] user successfully reset.
New value: bC*n=Lhk5E+NgdQUAS7L
[elasticsearch@f005f1289400 ~]$ 

Password changed to elastic/giraffe.


python elasticsearch Attempting to index the list of docs using helpers.bulk()
Error during bulk indexing: Connection error caused by: ConnectionError(Connection error caused by: ProtocolError(('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))))

ES log:

{"@timestamp":"2025-12-27T15:49:13.733Z", "log.level": "WARN", "message":"received plaintext http traffic on an https channel, closing connection Netty4HttpChannel{localAddress=/10.88.0.2:9200, remoteAddress=/192.168.127.1:49062}", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"elasticsearch[f005f1289400][transport_worker][T#3]","log.logger":"org.elasticsearch.http.netty4.Netty4HttpServerTransport","elasticsearch.cluster.uuid":"0T7n130JQFSyibKKyTuH7w","elasticsearch.node.id":"d6FAlYE-R6KBQw5Fg1UffQ","elasticsearch.node.name":"f005f1289400","elasticsearch.cluster.name":"docker-cluster"}


# Source - https://stackoverflow.com/a
# Posted by Anton, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-27, License - CC BY-SA 3.0

curl -X GET http://192.168.77.88:9200/_cat/indices


from browser, https://localhost:9200

{
  "name" : "f005f1289400",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "0T7n130JQFSyibKKyTuH7w",
  "version" : {
    "number" : "9.2.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "4ad0ef0e98a2e72fafbd79a19fa5cae2f026117d",
    "build_date" : "2025-11-06T22:07:39.673130621Z",
    "build_snapshot" : false,
    "lucene_version" : "10.3.1",
    "minimum_wire_compatibility_version" : "8.19.0",
    "minimum_index_compatibility_version" : "8.0.0"
  },
  "tagline" : "You Know, for Search"
}