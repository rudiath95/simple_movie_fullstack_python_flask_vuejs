<template>
  <div>
    <button type="button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">{{ msg }}</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Shark",
  data() {
    return {
      msg: "",
    };
  },
    created(){
        this.getResponse();
    },
  methods: {
    getResponse(){
      const path = 'http://localhost:5000/shark';
      axios.get(path)
            .then ((res) => { 
                console.log(res.data)
                this.msg = res.data;
            }) 
            .catch ((err) => {
                console.error(err);
            });
        },
    }
}
</script>