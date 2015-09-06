# ipynb_stripout

Output cells make it difficult to manage iPython notebooks under Git. Diffs become noisy and merge conflicts become common.

This has been adapted from cfriedline's [ipynb_template](https://github.com/cfriedline/ipynb_template) and minrk's original [gist](https://gist.github.com/minrk/6176788) with the goal of making output stripping as easy as possible.

## 1) Install (OS X)

First you need to install the `ipynb_stripout` script. Run the following from your terminal:

	wget -O /usr/local/bin/ipynb_stripout "https://raw.githubusercontent.com/jond3k/ipynb_stripout/master/ipynb_stripout"
	chmod +x /usr/local/bin/ipynb_stripout

## 2) Configure git

To make it optionally available to all your git repositories:

	git config --global filter.ipynb_stripout.clean ipynb_stripout
	git config --global filter.ipynb_stripout.smudge cat
	git config --global filter.ipynb_stripout.required
	

## 3) Add to repository

Go to the root of the repository you want to add it to and  `.gitattributes` with the following line:

	echo "*.ipynb filter=ipynb_stripout" >> .gitattributes
	
Now you can commit the attributes.

	git add .gitattributes
	git commit -m "Added ipynb_stripout. See https://github.com/jond3k/ipynb_stripout" .gitattributes 
