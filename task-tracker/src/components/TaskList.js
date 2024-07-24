import React from 'react';
import { List, ListItem, ListItemText, Typography } from '@mui/material';

const TaskList = ({ tasks }) => {
  return (
    <List>
      {tasks.length === 0 ? (
        <ListItem>
          <ListItemText>
            <Typography variant="body1" color="textSecondary">
              У вас пока нет задач. Добавьте новую задачу!
            </Typography>
          </ListItemText>
        </ListItem>
      ) : (
        tasks.map((task, index) => (
          <ListItem key={index}>
            <ListItemText primary={task} />
          </ListItem>
        ))
      )}
    </List>
  );
};

export default TaskList;
