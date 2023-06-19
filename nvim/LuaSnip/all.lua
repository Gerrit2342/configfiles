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

s({trig="mfg", snippetType="autosnippet"},
  fmta(
	[[
	Mit freundlichen Grüßen
	Gerrit Albert
	]],{}
      )
),

s({trig="VG", snippetType="autosnippet"},
  fmta(
	[[
	Viele Grüße
	Gerrit Albert
	]],{}
      )
),

s({trig="lg", snippetType="autosnippet"},
  fmta(
	[[
	Liebe Grüße
	Gerrit
	]],{}
      )
),

s({trig="unisig", snippetType="autosnippet"},
  fmta(
	[[
	--
	Gerrit M. Albert
	Wissenschaftlicher Mitarbeiter
	Fachstudienberater Technik
	
	RWTH Aachen
	Didaktik der Physik und Technik
	Modulbau Physik 2, Raum 003
	Otto-Blumenthal-Straße 20
	52074 Aachen
	]],{}
      )
),
s({trig="zb", snippetType="autosnippet"},
  fmta(
	[[
	z. B.
	]],{}
      )
),

s({trig="bf", snippetType="autosnippet"},
  fmta(
	"\\textbf{<>}",
	{i(1)}
      )
),

s({trig="it", snippetType="autosnippet"},
  fmta(
	"\\textit{<>}",
	{i(1)}
      )
)
}
