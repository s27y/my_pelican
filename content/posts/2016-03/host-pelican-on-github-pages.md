Title: Host Pelican on Github Pages
Date: 2016-3-6 20:12
Modified: 2016-3-6 20:12
Category: tech
Tags: pelican, blog,
Slug: host-pelican-on-github-pages
Authors: Yang Sun
Summary:
Status: 
disqus_identifier: yangsun.me/host-pelican-on-github-pages

Creating a blog can be easy, you can either choose a blog system then host yourself or using public blog hosting provider like [WordPress.com](https://wordpress.com), [Google Blogger](https://www.blogger.com/) and many other providers. If you like having flexibility and love playing with different technologies, a self-hosting blog might be your best choice. You can choice whatever technology you like and build a customized blog on it. If simplicity is your thing, then public blog provider is your first choice, all you need to worry about is what to write.

Other than the first two categories, there is a third option. You will have  the ability to customize your blog while the deployment process is still relatively simple. The static blog generator provides a good balance between flexibility and simplicity. There are many static blogs you can choice from. Check out the top popular static site generators ranked by [StaticGen](https://www.staticgen.com). 

Today what I am going to talk about is Pelican which is what beneath the blog you are reading. According to [Pelican Offical Website](http://blog.getpelican.com)
>Pelican is a static site generator, written in Python, that requires no database or server-side logic.

### How to setup Pelican 
#### Install pip
Download get-pip script from [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or run command in shell `curl -O https://bootstrap.pypa.io/get-pip.py`. After you have the script locally, run command `python get-pip.py`

##### Upgrade

If you already have pip installed and want to upgrade.
* On Linux or OS X: `pip install -U pip`
* On Windows: `python -m pip install -U pip`

#### Install virtualenv

>virtualenv is a tool to create isolated Python environments.

To install virtualenv and virtualenvwrapper, run `pip install virtualenvwrapper`, this command will install wirtualenvwrapper and all its dependencies.

##### Set up virtualenv with virtualenvwrapper

Once you have virtualenvwrapper installed, there are few more little things need be setup.

Simply add the lines below to your shell startup file (`.bashrc`, `.profile`, etc.)

```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

After updating the shell startup file, run command `source .bashrc` or ` source .profile`, this will load the new version of shell startup file. You can also reopen a terminal to pickup the changes.

##### How to use virtualenvwrapper?
* `workon` - list enviornments 
* `mkvirtualenv pelican` - create a new enviornment called pelican
* `workon pelican` -  activate the environment pelican
* `deactivated` - deactivate the working environment

#### Install Pelican

Before install pelican, make sure you have pip and virtualenvwarpper installed and setup.

* First activate a virtualenv you created in the previous step, `workon pelican`
* Install pelican using pip, `pip install pelican`
* If you want to use [Markdown](https://daringfireball.net/projects/markdown/) as markup format, install Markdown, `pip install Markdown`
* Choose a name for your project, create an appropriately-named directory for your project, and switch to that directory, 
```
mkdir -p ~/projects/yoursite
cd ~/projects/yoursite
```
* In your pelican project directory, create a pelican skeleton project via `pelican-quickstart`, you will be asked to enter some details about your setup.
* Your pelican project is ready to use. Start writing content under `yoursite/content` folder.

#### Github Pages

After setup my pelican on my local machine, I started to wonder where should I host my pelican blog? I found that the easiest way to host pelican is via [Github Pages](https://pages.github.com).

There are two kinds of Github Pages user site and project site. The process of setting up both kinds of Github Pages are very similar. 

* Create a Github repo for your pelican site
    * User page - create a repo named `username.github.io`, where username is your username (or organization name)
    * project page - create a repo or use your existing one. In the repository overview, click the branch drop-down on the left-hand side. Type in `gh-pages` and press enter. Now you have a branch called `gh-pages` created
* Go the `output` folder under your pelican project folder, and clone the repository
    * User page -`git clone -b my-branch https://git@github.com/username/myproject.git`
    * project page - `git clone https://github.com/username/username.github.io`
* Generate your pelican content by `pelican -s pelicanconf.py` or `pelican -s publishconf.py` to pick up the publish settings.
* Push it to Github
```
git add --all
git commit -m "Initial commit"
git push -u origin master
```
* Your pelican blog is now live! Check it on `username.github.io` or you project page.


#### Links
* [The Github repo host this blog](https://github.com/s27y/s27y.github.io)
* [Pelican Documentation](http://docs.getpelican.com/en/3.6.3/)