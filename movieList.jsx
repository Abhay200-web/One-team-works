import movieCard from "../movieCard"
import axios from "axios"
function MovieList(){
    return(
        <div>
            <h1>Movies</h1>
            <movieCard/>
        </div>
    )
}
export default MovieList;