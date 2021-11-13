import React, { Component } from "react"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeAssignment: {
        name: "",
        due_date: "",
        class_name: "",
        description: "",
        completed: false
      },
      assignmentList: []
    };
  }

  async componentDidMount() {
    try {
      const res = await fetch('http://localhost:8000/assignments/').then(results => results.json()).then(data => console.log(data));
      const assignmentList = await res.json();
      this.setState({
        assignmentList
      });
    } catch (e) {
      console.log(e);
    }
  }

  renderAssignments = () => {
    const { viewCompleted } = this.state;
    const newAssignments = this.state.assignmentList.filter(
      assignment => assignment.completed === viewCompleted
    );
    return newAssignments.map(assignment => (
      <li
        key={assignment.id}
        className="list-group-assignment d-flex justify-content-between align-assignments-center"
      >
        <span
          className={`todo-title mr-2 ${this.state.viewCompleted ? "completed-todo" : ""
            }`}
          title={assignment.description}
        >
          {assignment.title}
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="content">
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush">
                {this.renderAssignments()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    )
  }
}

export default App;
