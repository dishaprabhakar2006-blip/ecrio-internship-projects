from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():

    task_name = request.form.get('task')

    if task_name:
        tasks.append({
            'name': task_name,
            'done': False
        })

    return redirect('/')


@app.route('/complete/<int:index>')
def complete_task(index):

    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']

    return redirect('/')


@app.route('/delete/<int:index>')
def delete_task(index):

    if 0 <= index < len(tasks):
        tasks.pop(index)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)