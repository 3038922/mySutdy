module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: ['plugin:vue/essential', '@vue/standard'],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'space-before-function-paren': 0, //函数和参数空格0
    //忽略自己加逗号
    // 'comma-dangle': [
    // 	1,
    // 	{
    // 		objects: 'always',
    // 		arrays: 'ignore',
    // 		imports: 'ignore',
    // 		exports: 'ignore',
    // 		functions: 'ignore',
    // 	},
    // ],
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off'
  }
}
