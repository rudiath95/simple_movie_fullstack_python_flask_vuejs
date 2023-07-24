<template>
    <div class="p-4">
      <h2 class="text-2xl font-bold mb-4">Genre List</h2>
      <ConfirmationModal
        :is-open="isConfirmationModalOpen"
        :modal-name="modalToDeleteName" @confirmed="deleteConfirmed" @closed="closeConfirmationModal" />
    
      <div class="overflow-x-auto">
        <table class="w-full table-auto">
          <thead>
            <tr>
              <th class="px-4 py-2 bg-gray-100">ID</th>
              <th class="px-4 py-2 bg-gray-100 w-3/4">Name (Double Click to Edit)</th>
              <th class="px-4 py-2 bg-gray-100">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="genre in genres" :key="genre.id" class="hover:bg-gray-100">
                <td class="px-4 py-2">{{ genre.id }}</td>
                <td
                class="px-4 py-2"
                @dblclick="editGenreName(genre)"
                @click="selectText($event)"
                >
                <span v-if="!genre.editing" class="genre-name">{{ genre.name }}</span>
                <input
                    v-else
                    v-model="genre.name"
                    class="genre-input"
                    type="text"
                    :autofocus="genre.id === activeGenreId"
                    @blur="saveGenreName(genre)"
                    @keyup.enter="saveGenreName(genre)"
                />
                </td>
                <td class="px-4 py-2 flex items-center space-x-4">
                    <button
                    type="button"
                    class="flex items-center text-red-700 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-3 py-2 text-center"
                    @click="openConfirmationModal(genre.id, genre.name)"
                    >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-4 w-4 mr-2 -ml-0.5"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                        aria-hidden="true"
                    >
                    <path
                        fill-rule="evenodd"
                        d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                        clip-rule="evenodd"
                    />
                    </svg>
                    Delete
                </button>
                </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</template>


<script>
import axios from 'axios';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal,
  },
  data() {
    return {
      genres: [],
      isConfirmationModalOpen: false,
      genreToDeleteId: null,
      modalToDeleteName: '',
    };
  },
  mounted() {
    this.fetchGenres();
  },
  methods: {
    fetchGenres() {
      axios.get('http://localhost:5000/genre')
        .then(response => {
          this.genres = response.data.map(genre => ({
            ...genre,
            editing: false
          }));
        })
        .catch(error => {
          console.error('Error fetching genres:', error);
        });
    },
    editGenreName(genre) {
      genre.editing = true;
      this.activeGenreId = genre.id;
    },

    selectText(event) {
      if (!event.target.closest('input')) {
        const range = document.createRange();
        range.selectNodeContents(event.target);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
      }
    },
    saveGenreName(genre) {
      genre.editing = false;
      this.activeGenreId = null;
      axios
        .put(`http://localhost:5000/genre/${genre.id}`, { name: genre.name })
        .catch(error => {
          console.error('Error updating genre name:', error);
        });
    },

    openConfirmationModal(genreId, modalName) {
      this.isConfirmationModalOpen = true;
      this.genreToDeleteId = genreId;
      this.modalToDeleteName = modalName; 
      console.log(modalName);
    },

    closeConfirmationModal() {
      this.isConfirmationModalOpen = false;
      this.genreToDeleteId = null;
    },

    deleteConfirmed() {
      this.deleteGenre(this.genreToDeleteId);
    },

    deleteGenre(genreId) {
      axios
        .delete(`http://localhost:5000/genre/${genreId}`)
        .then(() => {
          this.genres = this.genres.filter(genre => genre.id !== genreId);
        })
        .catch(error => {
          console.error('Error deleting genre:', error);
        });
    },
  },
};
</script>


<style>
.genre-name {
    display: inline;
}
</style>