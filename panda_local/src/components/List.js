import React from 'react';
const List = (props) => {
  const { repos } = props;

  if (!repos || repos.length === 0) return <p>No Tournaments entered by that player, sorry</p>;
  return (
    <ul>
      <h2 className='list-head'>Tournament Placings by that Player</h2>
      {repos.map((repo) => {
        return (
          <li key={repo.id} className='list'>
            <span className='repo-text'>{repo.key} </span>
            <span className='repo-description'>{repo.placing}</span>
          </li>
        );
      })}
    </ul>
  );
};
export default List;