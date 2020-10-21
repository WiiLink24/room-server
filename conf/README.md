### What is first.bin?
`first.bin` is a file initially served as configuration pointing to URLs the channel should request.

Despite it being XML internally, the file is encrypted. It's unknown why this design was chosen,
as the file was served over HTTPS by Nintendo. AES is symmetric and provides no method of signing. Additionally, the
keys are easily found within the channel's contents.

If you want to run `room-server` separately for use with Wii no Ma, you must edit and create a first.bin.

### How to create a first.bin

This is AES-128-CBC encrypted, using keys available within the app's main arc.

To decrypt an existing one:
```
openssl aes-128-cbc -d -in first.bin -out first.txt -K 943B13DD87468BA5D9B7A8B899F91803 -iv 66B33FC1373FE506EC2B59FB6B977C82
```

To encrypt:
```
openssl aes-128-cbc -d -in first.txt -out first.bin -K 943B13DD87468BA5D9B7A8B899F91803 -iv 66B33FC1373FE506EC2B59FB6B977C82
```
