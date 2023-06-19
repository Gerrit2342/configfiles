local ls = require("luasnip")
local s = ls.snippet
local sn = ls.snippet_node
local t = ls.text_node
local i = ls.insert_node
local f = ls.function_node
local d = ls.dynamic_node
local fmt = require("luasnip.extras.fmt").fmt
local fmta = require("luasnip.extras.fmt").fmta
local rep = require("luasnip.extras").rep

return {
-- Examples of complete snippets using fmt and fmta

s({trig="for", snippetType="autosnippet"},
  fmta(
    [[
	for(int <>; <>; <>){
          <>
	}
    ]],
    {
      i(1, "start"),
      i(2, "bis"),
      i(3, "inkrement"),
      i(4),
    }
  )
)
}
