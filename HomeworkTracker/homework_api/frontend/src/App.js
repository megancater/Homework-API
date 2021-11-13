import React, { Component } from "react"
import Modal from "./components/Modal";
import axios from "axios";
class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            viewCompleted: false,
            activeAssignment: {
                id: "",
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
        fetch('http://localhost:8000/assignments/')
            .then(res => res.json())
            .then((data) => {
                this.setState({ assignmentList: data.results })
            })
            .catch(console.log);
    }

    toggle = () => {
        this.setState({ modal: !this.state.modal });
    }

    handleSubmit = assignment => {
        this.toggle();
        if (assignment.id) {
            axios
                .put(`'http://localhost:8000/assignments/${assignment.id}/'`, assignment)
            return;
        }
        axios
            .post("http://localhost:8000/assignments/", assignment)
    };

    createAssignment = () => {
        const assignment = { name: "", description: "", completed: false };
        this.setState({ activeAssignment: assignment, modal: !this.state.modal });
    };

    displayCompleted = status => {
        if (status) {
            return this.setState({ viewCompleted: true });
        }
        return this.setState({ viewCompleted: false });
    };

    renderTabList = () => {
        return (
            <div className="my-5 tab-list">
                <button
                    onClick={() => this.displayCompleted(true)}
                    className={this.state.viewCompleted ? "active" : ""}
                >
                    Complete
                </button>
                <button
                    onClick={() => this.displayCompleted(false)}
                    className={this.state.viewCompleted ? "" : "active"}
                >
                    Incomplete
                </button>
            </div>
        );
    };

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
                    title={assignment.name}
                >
                    {assignment.name} | {assignment.description}
                </span>
            </li>
        ));
    };

    render() {
        return (
            <main className="content">
                <h1 className="text-white text-uppercase text-center my-4">Homework Tracker</h1>
                <div className="row">
                    <div className="col-md-6 col-sm-10 mx-auto p-0">
                        <div className="card p-3">
                            <div className="">
                                <button onClick={this.createAssignment} className="btn btn-success">Add Task</button>
                            </div>
                            <ul className="list-group list-group-flush">
                                {this.renderAssignments()}
                            </ul>
                        </div>
                    </div>
                </div>
                {this.state.modal ? (
                    <Modal
                        activeAssignment={this.state.activeAssignment}
                        toggle={this.toggle}
                        onSave={this.handleSubmit}
                    />
                ) : null}
            </main>
        )
    }
}

export default App;
