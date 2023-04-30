import React from 'react';

function SearchBar() {
  const handleButtonClick = async () => {
    const data = {
      // can you add a boolean to determine if a user wants to recommend a movie based off video games or vice versa?
      // Ex: isMovie : (false or true)
      // if false: endpoint is /recommendGames
      movie: "Toy Story (1995)",
    };

    try {
      const response = await fetch("http://192.168.1.23:5000/recommendGames", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <button onClick={handleButtonClick}>Recommend</button>
    </div>
  );
}

export default SearchBar;



// import React from "react";

// const SearchBar = ({keyword, onChange}) => {
//     const BarStyle = {width:"15rem", padding:"0.35rem", border:"none", };
//     return (
//       <input 
//        style={BarStyle}
//        key="search-bar"
//        placeholder={"Type Your Movie or Game Here"}
//        value={keyword}
//        onChange={(event) => onChange(event.target.value)}
//       />
//     );
//   }

// export default SearchBar;