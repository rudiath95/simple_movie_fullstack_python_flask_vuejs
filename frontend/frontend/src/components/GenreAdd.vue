<template>
    <div class="p-4">
      <form @submit.prevent="addGenre">
        <div class="mb-4 relative ">
          <input
            id="genreName"
            v-model="newGenreName"
            type="text"
            name="genreName"
            placeholder="Genre Name"
            class="mt-1 px-4 py-2 w-full border border-gray-300 rounded-md focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            required
          />
          <button
            type="button"
            class="absolute top-1 right-0 mr-2 px-4 py-2 text-gray-500 font-medium"
            @click="cancelAdd"
          >
            X
          </button>
        </div>
        <div class="flex justify-end">
          
          <button
            type="submit"
            class="px-4 py-2 text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            @click="addGenre"
            >
            Add Genre
          </button>
        </div>
      </form>
    </div>
  </template>
  
<script>
import axios from 'axios';

export default {
data() {
    return {
    newGenreName: '',
    };
},
methods: {
    addGenre() {
    const genreData = { name: this.newGenreName };
    axios
        .post('http://localhost:5000/genre', genreData)
        .then(response => {
        console.log('Genre added successfully:', response.data);
        this.newGenreName = '';
        })
        .catch(error => {
        console.error('Error adding genre:', error);
        });
        this.$emit('genre-added');
    },
    cancelAdd() {
    this.newGenreName = '';
    this.$emit('cancelled');
    },
},
};
</script>

