import './App.css';
import React, { useState } from 'react';
import { Container, Typography, AppBar, Toolbar } from '@mui/material';
import TaskList from './components/TaskList';
import TaskForm from './components/TaskForm';

const App = () => {
  const [tasks, setTasks] = useState([]);

  const addTask = (task) => {
    setTasks([...tasks, task]);
  };

  return (
    <Container maxWidth="sm">
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Task Tracker</Typography>
        </Toolbar>
      </AppBar>
      <TaskForm addTask={addTask} />
      <TaskList tasks={tasks} />
    </Container>
  );
};

export default App;
