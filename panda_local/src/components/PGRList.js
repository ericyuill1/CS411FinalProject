import React from 'react';
import react from 'react';
import styles from "./HeadToHeadList.module.css";
const PGRList = (props) => {
  const { resp } = props;
  if (!resp || resp.length === 0) return <p>No Tournaments entered by that player, sorry</p>;
  return (
      <table className ={styles.table} key="PGR table">
          <thead>
        <tr>
            <th>Player</th>
            <th>Ranking</th> 
        </tr>
        </thead>
        <tbody>
        {resp.map((repo, i) => {
            return (
            <tr key={repo.key} className='l'>
                <td key={repo.Player}>{repo.Player}</td>
                <td key={repo.Elo}>{repo.Elo} </td>
            </tr>
            );
        })}
        </tbody>
      </table>
  );
};
export default PGRList;