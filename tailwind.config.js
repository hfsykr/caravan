/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      height: {
        '112': '28rem',
      }
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
  darkMode: 'class'
}