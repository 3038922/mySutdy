module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ["plugin:vue/essential", "@vue/standard"],
  parserOptions: {
    parser: "babel-eslint",
  },
  rules: {
    // quotes: [1, "single"], //忽略引号 引号类型 `` "" ''
    // "space-before-function-paren": 0, //函数和参数空格0
    // "eol-last": 0, //忽略末行空格
    // "no-multiple-empty-lines": ["error", { max: 1, maxEOF: 0 }], //忽略末行空格
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
  },
};
