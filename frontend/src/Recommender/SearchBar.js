import React from "react";

const SearchBar = ({keyword, onChange}) => {
    const BarStyle = {width:"15rem", padding:"0.35rem", border:"none", };
    return (
      <input 
       style={BarStyle}
       key="search-bar"
       placeholder={"Type Here"}
       value={keyword}
       onChange={(event) => onChange(event.target.value)}
      />
    );
  }

export default SearchBar;