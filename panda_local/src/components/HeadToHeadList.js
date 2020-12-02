import React from 'react';
import react from 'react';
import styles from "./HeadToHeadList.module.css";
const HeadToHeadList = (props) => {
  const { repos } = props;
  if (!repos || repos.length === 0) return <p>No Tournaments entered by that player, sorry</p>;
  return (
      <table>
        <tr>
            <th>Player 1 Placement</th>
            <th>Tournament Name</th> 
            <th>Player 2 Placement</th>
        </tr>
      
        {repos.map((repo) => {
            return (
            <tr key={repo.id} className='list'>
                <td >{repo.placings[0]}</td>
                <td >{repo.tournament} </td>
                <td >{repo.placings[1]}</td>
            </tr>
            );
        })}
      </table>
    // <ul>
    //   <h2 className='list-head'>Tournament Placings by that Player</h2>
    //   {repos.map((repo) => {
    //     return (
    //       <li key={repo.id} className='list'>
    //         <span className={styles.span}>{repo.placings[0]}</span>
    //         <span className={styles.span}>{repo.tournament} </span>
    //         <span className={styles.span}>{repo.placings[1]}</span>
    //       </li>
    //     );
    //   })}
    // </ul>
  );
};
export default HeadToHeadList;