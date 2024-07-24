import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';

const TaskForm = ({ addTask }) => {
  const [taskName, setTaskName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!taskName) return;
    addTask({ name: taskName, id: Date.now() });
    setTaskName('');
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ my: 2 }}>
      <TextField
        label="New Task"
        variant="outlined"
        fullWidth
        value={taskName}
        onChange={(e) => setTaskName(e.target.value)}
      />
      <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
        Add Task
      </Button>
    </Box>
  );
};

export default TaskForm;
