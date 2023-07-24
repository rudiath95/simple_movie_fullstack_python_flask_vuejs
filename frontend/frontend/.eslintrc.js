module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  rules: {
    'vue/multi-word-component-names': 'off',
    'no-console': 'off',
  },
  extends: [
    '@nuxtjs/eslint-config-typescript',
    'plugin:nuxt/recommended',
    'prettier',
  ],
  plugins: [],
};
