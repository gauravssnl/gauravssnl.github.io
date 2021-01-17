Title: Rust Development Environment Setup
Date: 2020-10-26 09:40
Author: gauravssnl
Category: Uncategorized
Tags: Rust, Windows
Slug: rust-development-environment-setup
Status: published

In this post, I am going to share how to set up a system for Rust development. This tutorial can be used either on Windows OS or on Linux OS.

# Steps

1\.  Install **rustup** which will install the **rustc** , **cargo** and other things required for Rust from its official website ( <https://www.rust-lang.org/tools/install> ) .

2\.  Configure the PATH variable of your system so that you can invoke **rustc** , **cargo** and other rust related commands. Verify it by invoking these commands in terminal.

3\.  The successful installation of Rust can also be verified by invoking the command :

```bash
rustc --version
```

4\. If you are a Windows OS user, please install the  [Visual Studio C++ Build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) . You can also read my [previous post](https://gauravssnl.wordpress.com/2020/06/24/install-visual-studio-for-c-c-and-rust-development-on-windows-os/) regarding this, if you want to know the setup steps in details .

5\.  The next step is to verify that we are able to compile a HelloWorld program. To do that we can either manually write a Hello World program or use **cargo** to generate it. I will be using **cargo** to make this simple. To do that, use the command :

```bash
cargo new hello
```

6\.  Navigate to the newly created directory ( hello in this case), and try compiling and running the program : 
```bash 
cargo build && cargo run
```

![Compiling and running a simple Rust program](https://gauravssnl.files.wordpress.com/2020/10/image.png?w=603)

7\. Now, we need to setup a Text Editor for Rust development or we can use IDE. I prefer using Text Editor and I am using VSCode ([Visual Studio Code](https://code.visualstudio.com/)) now a days. So, I will be setting up VSCode for Rust development such as syntax highlighting, auto completion, etc.

8\. Open VSCode and click on Extensions and install the **[Rust Extension](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust)** .

9\. Restart the VSCode and start working with Rust code and projects and we will see the features of auto completion, syntax highlighting, etc.

![VSCode Rust Extension screenshot](https://gauravssnl.files.wordpress.com/2020/10/image-2.png?w=1024)

10\. Enjoy Rust programming and keep on learning Rust now :)

I hope this tutorial will be useful to you all. Let me know if you have any questions regarding this tutorial or if you want to ask me anything about Rust. You can also reach out to me through [my Twitter account](https://twitter.com/gauravssnl).

