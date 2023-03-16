module.exports = {
  env: {
    browser: true,
    es2022: true,
    node: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:prettier/recommended",
  ],
  ignorePatterns: ["node_modules/", "*.test.js"],
  overrides: [
    {
      files: ["**/*.jsx"],
      rules: {
        "no-unused-vars": ["error", { varsIgnorePattern: "^React$" }],
      },
    },
  ],
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: "module",
  },
  plugins: ["react"],
  rules: {
    "react/jsx-uses-react": "off",
    "react/jsx-uses-vars": "error",
    "react/react-in-jsx-scope": "error",
    "react/prop-types": "off",
  },
};
