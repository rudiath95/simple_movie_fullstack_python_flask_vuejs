<template>
    <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
      <div class="bg-white p-8 rounded-lg shadow-md">
        <h3 class="text-xl font-semibold mb-4">Confirm Deletion</h3>
        <p class="mb-4">Are you sure you want to delete <span class="font-bold text-blue-500">"{{ modalName }}"</span>?</p>
        <div class="flex justify-end">
          <button class="text-gray-500 px-4 py-2 mr-2" @click="closeModal">Cancel</button>
          <button class="text-red-700 px-4 py-2" @click="confirmDeletion">Delete</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isOpen: Boolean,
      modalName: String,
    },
    data() {
      return {
        isModalOpen: false,
      };
    },
    watch: {
      isOpen: {
        immediate: true,
        handler(newVal) {
          this.isModalOpen = newVal;
        },
      },
    },
    methods: {
      closeModal() {
        this.isModalOpen = false;
        this.$emit('closed');
      },
      confirmDeletion() {
        this.$emit('confirmed');
      },
    },
  };
  </script>
  