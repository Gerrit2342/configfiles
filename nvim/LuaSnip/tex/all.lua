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

-- \texttt
s({trig="pp", dscr="'\\usepackage{} einfuegen'", snippetType="autosnippet"},
  fmta(
    "\\usepackage{<>}",
    { i(1) }
  )
),

-- Zitationsbefehle
s({trig="cc", dscr="\\autocite{} einfuegen", snippetType="autosnippet"},
  fmta(
    "\\autocite[<>][<>]{<>}",
    { i(2, "vgl." ),
    i(3, "S."),
    i(1, "Autor"),
    }
  )
),

s({trig="ct", dscr="\\textcite{} einfuegen", snippetType="autosnippet"},
  fmta(
    "\\textcite[<>][<>]{<>}",
    { i(2, "vgl." ),
    i(3, "S."),
    i(1, "Autor"),
    }
  )
),


-- s({trig="cp", dscr="\\parencite{} einfuegen", snippetType="autosnippet"},
--   fmta(
--     "\\parencite[<>][<>]{<>}",
--     { i(2, "vgl." ),
--     i(3, "S."),
--     i(1, "Autor"),
--     }
--   )
-- ),


s({trig="LL", dscr="'\\label{} einfuegen'", snippetType="autosnippet"},
  fmta(
    "\\label{<>}",
    { i(1) }
  )
),

s({trig="ref", dscr="'\\ref{} einfuegen'", snippetType="autosnippet"},
  fmta(
    "(Abb. \\ref{<>})",
    { i(1) }
  )
),

s({trig="to", dscr="'\\todo{} einfuegen'", snippetType="autosnippet"},
  fmta(
    "\\todo{<>}",
    { i(1) }
  )
),
s({trig="SS", dscr="'\\section{} einfuegen'", snippetType="autosnippet"},
  fmta(
    "\\section{<>}",
    { i(1) }
  )
),

s({trig="BE", snippetType="autosnippet"},
  fmta(
    [[
      \begin{<>}
          <>
      \end{<>}
    ]],
    {
      i(1),
      i(2),
      rep(1),  -- this node repeats insert node i(1)
    }
  )
),

s({trig="fig", snippetType="autosnippet"},
  fmta(
    [[
      \begin{figure}[h]
      \centering
      \includegraphics{<>}
      \caption{<>}
      \label{<>}
      \end{figure}
    ]],
    {
      i(1),
      i(2),
      i(3),
    }
  )
)
}
