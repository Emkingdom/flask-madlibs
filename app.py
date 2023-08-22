from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stoires_madlibs import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/form-story")
def form_story():
    return render_template("form-story.html")


@app.route("/stories")
def stories():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")

    story = Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

    story_words = {"place": place, "noun": noun, "verb": verb,
                   "adjective": adjective, "plural_noun": plural_noun}
    complete_story = story.generate(story_words)

    return render_template("stories.html", complete_story=complete_story)
