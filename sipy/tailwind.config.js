/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html', // Include app-level templates
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#0066cc', // Default shade
        },
        secondary: {
          DEFAULT: '#99cc01', // Default shade
          light:'#F18701'
        },
      },
      fontFamily: {
        title: ['Figtree', 'sans-serif'],  // Title font (Figtree)
        subheading: ['poppins', 'sans-serif'],  // Subheading font (Poppins)
        body: ['Darker Grotesque', 'sans-serif'],  // Body font (Darker Grotesque)
      },
    },
  },
  plugins: [],
};
