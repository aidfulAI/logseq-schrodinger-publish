# logseq-schrodinger-publish
This python scripts helps in publishing your public logseq pages as static Hugo website with [logseq-schrodinger](https://github.com/sawhney17/logseq-schrodinger).

# It does the following
1. Delete the pages and assets folder in your target path (to avoid that renamed files are published twice or pages turned private are published).
2. Unzips your logseq-schrodinger export to your local github directory.
3. Delete the exported zip file (to avoid the overwrite dialog while exporting)

# Usage
1. Copy the `config.ini.sample` file to `config.ini` and rename the variables according to your setup
2. Run the script

# Contact
Daniel Bender - [@aidfulai](https://twitter.com/aidfulai)

# Acknowledgement
Thanks to Aryan Sawhney [@aryansawhney17](https://twitter.com/aryansawhney17) who builds amazing logseq plugins including logseq-schrodinger. Your rock!

