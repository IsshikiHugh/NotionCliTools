# NotionCliTools

I try to create a CLI tool to take quick notes. Although we have tools like flomo, which provide powerful 'quick notes' function, it will be not very convenient if we want to take lots of notes with same form. Because we should take more efforts to change the plain text to forms.

So, I consider to use Notion's database to organize such notes. For examples, a word cards which allows me to quick insert words met in daily learning or reading.

## Install & Use

1. Clone the repo:

```bash
git clone git@github.com:IsshikiHugh/NotionCliTools.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the `config.yaml.example` file to `config.yaml` and fill in the blanks.

- You can get `notion-token` [here](https://www.notion.so/my-integrations).
- The app's related db should have the same structure as the forms. But the name of the column doesn't matter (which you should fill in).

4. Run the following command.

```bash
python src/main.py
```

- [ ] I will make these more detailed latter.
