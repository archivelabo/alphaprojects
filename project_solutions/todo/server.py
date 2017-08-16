from flask import Flask, request
from flask import render_template_string
from flask import redirect

import os, re

app = Flask(__name__)


class Task:
    def __init__(self, content, complete):
        self.text = content
        self.done = complete

@app.route('/')
def tasks_list():
    tasks = []
    db = open('db.csv', 'r')
    for row in db:
        row = row.split(',')
        tasks.append(Task(row[0], row[1].rstrip()))
    html = """<ul>
{% for task in tasks %}
    <li>
        {% if task.done == '1' %} <strike> {% endif %}{{ task.text }} {% if task.done == '1'%} </strike>{% endif %}
        <a href="#" onclick="goto('/done/'+ '{{ task.text }}')">X</a>
        <a href="#" onclick="goto('/delete/' + '{{ task.text }}')">Delete</a>
    </li>
{% endfor %}
</ul>


<form method="post" onsubmit="get_action(this);">
    <p><input type="text" name="content" required></p>
    <input type="submit" value="Add task">
</form>

<script>

    function get_action(form) {
        form.action = window.location.pathname + "/task" + window.location.pathname;
     }
function goto(url){window.location.href=window.location.href.substr(0, window.location.href.lastIndexOf("0") + 1) + '/' + url + '/' + window.location.pathname}

</script>"""
    return render_template_string(html, tasks=tasks)


@app.route('/task/<string:path>', methods=['POST'])
def add_task(path):
    content = request.form['content']
    if not content:
        return 'Error'
    task = Task(content, 0)
    db = open('db.csv', 'a')
    db.write(task.text + "," + str(task.done) + "\n")
    print(request.url.replace("http", "https")[31:])
    print(path)
    return redirect(request.url.replace("http", "https").replace("task/", ""))


@app.route('/delete/<string:content>/<string:path>')
def delete_task(content, path):
    db = open('db.csv', 'r')
    db_new = open('db_new.csv', 'w')
    for row in db:
        if content not in row:
            db_new.write(row)

    os.remove('db.csv')
    os.rename('db_new.csv', 'db.csv')
    return redirect(re.sub(r"delete/(.+)/", "", request.url.replace("http", "https")))


@app.route('/done/<string:content>/<string:path>')
def resolve_task(content, path):
    db = open('db.csv', 'r')
    db_new = open('db_new.csv', 'w')
    for row in db:
        if content not in row:
            db_new.write(row)
        else:
            if int(row[-2]):
                db_new.write(row[:-2] + '0\n')
            else:
                db_new.write(row[:-2] + '1\n')

    os.remove('db.csv')
    os.rename('db_new.csv', 'db.csv')
    return redirect(re.sub(r"done/(.+)/", "", request.url.replace("http", "https")))


if __name__ == '__main__':
    app.run()
