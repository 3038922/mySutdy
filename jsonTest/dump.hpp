#pragma once
#include "./json.hpp"
void dump(const json &val, std::string_view ignore)
{
    switch (val.m_type)
    {
        case json::value_t::object: {
            if (val.m_value.object->empty())
            {
                o->write_characters("{}", 2);
                return;
            }

            if (pretty_print)
            {
                o->write_characters("{\n", 2);

                // variable to hold indentation for recursive calls
                const auto new_indent = current_indent + indent_step;
                if (JSON_HEDLEY_UNLIKELY(indent_string.size() < new_indent))
                {
                    indent_string.resize(indent_string.size() * 2, ' ');
                }

                // first n-1 elements
                auto i = val.m_value.object->cbegin();
                for (std::size_t cnt = 0; cnt < val.m_value.object->size() - 1; ++cnt, ++i)
                {
                    o->write_characters(indent_string.c_str(), new_indent);
                    o->write_character('\"');
                    dump_escaped(i->first, ensure_ascii);
                    o->write_characters("\": ", 3);
                    dump(i->second, true, ensure_ascii, indent_step, new_indent);
                    o->write_characters(",\n", 2);
                }

                // last element
                JSON_ASSERT(i != val.m_value.object->cend());
                JSON_ASSERT(std::next(i) == val.m_value.object->cend());
                o->write_characters(indent_string.c_str(), new_indent);
                o->write_character('\"');
                dump_escaped(i->first, ensure_ascii);
                o->write_characters("\": ", 3);
                dump(i->second, true, ensure_ascii, indent_step, new_indent);

                o->write_character('\n');
                o->write_characters(indent_string.c_str(), current_indent);
                o->write_character('}');
            }
            else
            {
                o->write_character('{');

                // first n-1 elements
                auto i = val.m_value.object->cbegin();
                for (std::size_t cnt = 0; cnt < val.m_value.object->size() - 1; ++cnt, ++i)
                {
                    o->write_character('\"');
                    dump_escaped(i->first, ensure_ascii);
                    o->write_characters("\":", 2);
                    dump(i->second, false, ensure_ascii, indent_step, current_indent);
                    o->write_character(',');
                }

                // last element
                JSON_ASSERT(i != val.m_value.object->cend());
                JSON_ASSERT(std::next(i) == val.m_value.object->cend());
                o->write_character('\"');
                dump_escaped(i->first, ensure_ascii);
                o->write_characters("\":", 2);
                dump(i->second, false, ensure_ascii, indent_step, current_indent);

                o->write_character('}');
            }

            return;
        }

        case value_t::array: {
            if (val.m_value.array->empty())
            {
                o->write_characters("[]", 2);
                return;
            }

            if (pretty_print)
            {
                o->write_characters("[\n", 2);

                // variable to hold indentation for recursive calls
                const auto new_indent = current_indent + indent_step;
                if (JSON_HEDLEY_UNLIKELY(indent_string.size() < new_indent))
                {
                    indent_string.resize(indent_string.size() * 2, ' ');
                }

                // first n-1 elements
                for (auto i = val.m_value.array->cbegin();
                     i != val.m_value.array->cend() - 1; ++i)
                {
                    o->write_characters(indent_string.c_str(), new_indent);
                    dump(*i, true, ensure_ascii, indent_step, new_indent);
                    o->write_characters(",\n", 2);
                }

                // last element
                JSON_ASSERT(!val.m_value.array->empty());
                o->write_characters(indent_string.c_str(), new_indent);
                dump(val.m_value.array->back(), true, ensure_ascii, indent_step, new_indent);

                o->write_character('\n');
                o->write_characters(indent_string.c_str(), current_indent);
                o->write_character(']');
            }
            else
            {
                o->write_character('[');

                // first n-1 elements
                for (auto i = val.m_value.array->cbegin();
                     i != val.m_value.array->cend() - 1; ++i)
                {
                    dump(*i, false, ensure_ascii, indent_step, current_indent);
                    o->write_character(',');
                }

                // last element
                JSON_ASSERT(!val.m_value.array->empty());
                dump(val.m_value.array->back(), false, ensure_ascii, indent_step, current_indent);

                o->write_character(']');
            }

            return;
        }

        case value_t::string: {
            o->write_character('\"');
            dump_escaped(*val.m_value.string, ensure_ascii);
            o->write_character('\"');
            return;
        }

        case value_t::binary: {
            if (pretty_print)
            {
                o->write_characters("{\n", 2);

                // variable to hold indentation for recursive calls
                const auto new_indent = current_indent + indent_step;
                if (JSON_HEDLEY_UNLIKELY(indent_string.size() < new_indent))
                {
                    indent_string.resize(indent_string.size() * 2, ' ');
                }

                o->write_characters(indent_string.c_str(), new_indent);

                o->write_characters("\"bytes\": [", 10);

                if (!val.m_value.binary->empty())
                {
                    for (auto i = val.m_value.binary->cbegin();
                         i != val.m_value.binary->cend() - 1; ++i)
                    {
                        dump_integer(*i);
                        o->write_characters(", ", 2);
                    }
                    dump_integer(val.m_value.binary->back());
                }

                o->write_characters("],\n", 3);
                o->write_characters(indent_string.c_str(), new_indent);

                o->write_characters("\"subtype\": ", 11);
                if (val.m_value.binary->has_subtype())
                {
                    dump_integer(val.m_value.binary->subtype());
                }
                else
                {
                    o->write_characters("null", 4);
                }
                o->write_character('\n');
                o->write_characters(indent_string.c_str(), current_indent);
                o->write_character('}');
            }
            else
            {
                o->write_characters("{\"bytes\":[", 10);

                if (!val.m_value.binary->empty())
                {
                    for (auto i = val.m_value.binary->cbegin();
                         i != val.m_value.binary->cend() - 1; ++i)
                    {
                        dump_integer(*i);
                        o->write_character(',');
                    }
                    dump_integer(val.m_value.binary->back());
                }

                o->write_characters("],\"subtype\":", 12);
                if (val.m_value.binary->has_subtype())
                {
                    dump_integer(val.m_value.binary->subtype());
                    o->write_character('}');
                }
                else
                {
                    o->write_characters("null}", 5);
                }
            }
            return;
        }

        case value_t::boolean: {
            if (val.m_value.boolean)
            {
                o->write_characters("true", 4);
            }
            else
            {
                o->write_characters("false", 5);
            }
            return;
        }

        case value_t::number_integer: {
            dump_integer(val.m_value.number_integer);
            return;
        }

        case value_t::number_unsigned: {
            dump_integer(val.m_value.number_unsigned);
            return;
        }

        case value_t::number_float: {
            dump_float(val.m_value.number_float);
            return;
        }

        case value_t::discarded: {
            o->write_characters("<discarded>", 11);
            return;
        }

        case value_t::null: {
            o->write_characters("null", 4);
            return;
        }

        default:                // LCOV_EXCL_LINE
            JSON_ASSERT(false); // LCOV_EXCL_LINE
    }
}