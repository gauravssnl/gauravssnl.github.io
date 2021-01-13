Title: Rust - How to read all the data of a   TcpStream (socket) completely ?
Date: 2020-11-03 11:47
Author: gauravssnl
Category: Networking, Uncategorized
Tags: Newtork Programming, Rust, Socket, TcpStream
Slug: rust-how-to-read-all-the-data-of-a-tcpstream-socket-completely
Status: published

`<!-- wp:paragraph -->`{=html}

Hi everyone. I have started learning Rust and I tried creating a project [RServer](https://github.com/gauravssnl/rserver) which is an app for intercepting/capturing TCP requests sent by browser and other apps running on a system. While developing [RServer](https://github.com/gauravssnl/rserver) , I faced an issue while trying to read the complete data from a [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html) struct. [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html) has only [read](https://doc.rust-lang.org/std/net/struct.TcpStream.html#impl-Read) method , but socket /TCP streams constructs do not have method such as **read_all** to read all the data from the stream. In this post, I am going to share my technique which I used in [RServer](https://github.com/gauravssnl/rserver) .

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

As we do not have any built-in method to read the [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html) completely in one go , we obviously need to use some kind of loop to read the complete data from a given stream. Let us consider that we want to read all the data and we need to return the data and its length/size.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:html -->`{=html}

    [sourcecode language="python" wraplines="false" collapse="false"]
    /// Read the stream data and return stream data & its length
    fn read_stream(stream: &mut TcpStream) -> (Vec, usize) {
        let buffer_size = 512;
        let mut request_buffer = vec![];
        // let us loop & try to read the whole request data
        let mut request_len = 0usize;
        loop {
            let mut buffer = vec![0; buffer_size];
            match stream.read(&mut buffer) {
                Ok(n) => {
                   
                    if n == 0 {
                        break;
                    } else {
                        request_len += n;

                        // we need not read more data in case we have read less data than buffer size
                        if n  {
                    println!("Error in reading stream data: {:?}", e);
                    break;
                }
            }
        }

        (request_buffer, request_len)
    }
    [/sourcecode]

`<!-- /wp:html -->`{=html}

`<!-- wp:paragraph -->`{=html}

Explanation :

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I have taken an initial buffer size as 512 as an example, we will be reading 512 bytes or lesser in one go from the stream. I have taken a mutable Vector here as we cannot determine the [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html) data size/length in advance as we are reading data via network. Most of the other examples available might be using an array, but that might lead to either wastage of some space or there will be space scarcity to read all the data and store the data into the array as the size might be more or lesser than the required space. I am storing the length of the data which we read in a variable **request_len** .

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I am using a mutable temporary Vector variable buffer and try reading the 512 bytes inside a loop, then we are using a match pattern while reading the data to know the number of bytes of data which were read. Depending on the number of bytes read from [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html), which is n here, the corresponding code placed in the arm of the match block will be executed. If n is 0, i.e there is no data and nothing was read, we just need to break out of the loop and stop reading the stream. Otherwise, we just add the number of bytes read to the variable **request_len** . If n is lesser than the buffer size (512 here), we understand that the Stream has lesser data than our buffer size, we add the data how much ever it was there , by adding the **mut buffer\[..n\]** to the mutable vector **request_buffer** and then we break out of the loop as we have no more data under the current iteration of the loop. If n is equal to our buffer size ( 512 here), we read the data and add the data into mutable vector **request_buffer** . In this case, we don't break out of the loop and try reading more data out of the [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html) if available .

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I hope this post will be useful to you all who are learning Rust [socket](https://en.wikipedia.org/wiki/Network_socket) / [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html) programming . The same concept can be used for reading data from [socket](https://en.wikipedia.org/wiki/Network_socket) in other languages too. Thanks for reading the post. Please post your questions and ideas in comments. Feel free to reach out to me if you have better ways of doing this or for any questions. Follow me on [Twitter](https://twitter.com/gauravssnl) for more updates and if you want to connect with me.

`<!-- /wp:paragraph -->`{=html}
