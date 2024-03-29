// Generated from /home/subadmin/Desktop/AGH/SEM5/KOMPILATORY/<C>/repo/GeneriC/generated/par.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class par extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		RETURN=1, SEMICOLON=2, BRACKET_OR=3, BRACKET_CR=4, BRACKET_OS=5, BRACKET_CS=6, 
		BRACKET_OW=7, BRACKET_CW=8, COMMA=9, EQUAL=10, IDENTIFIER=11, TYPE_IDENTIFIER=12, 
		WS=13;
	public static final int
		RULE_program = 0, RULE_function = 1, RULE_head = 2, RULE_type_parameters = 3, 
		RULE_type_params = 4, RULE_args = 5, RULE_statement = 6, RULE_return_s = 7, 
		RULE_assign_s = 8, RULE_init_s = 9, RULE_type = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "function", "head", "type_parameters", "type_params", "args", 
			"statement", "return_s", "assign_s", "init_s", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'return'", "';'", "'('", "')'", "'<'", "'>'", "'{'", "'}'", "','", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "RETURN", "SEMICOLON", "BRACKET_OR", "BRACKET_CR", "BRACKET_OS", 
			"BRACKET_CS", "BRACKET_OW", "BRACKET_CW", "COMMA", "EQUAL", "IDENTIFIER", 
			"TYPE_IDENTIFIER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "par.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public par(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(par.EOF, 0); }
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER || _la==TYPE_IDENTIFIER) {
				{
				{
				setState(22);
				function();
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(28);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public HeadContext head() {
			return getRuleContext(HeadContext.class,0);
		}
		public TerminalNode BRACKET_OW() { return getToken(par.BRACKET_OW, 0); }
		public TerminalNode BRACKET_CW() { return getToken(par.BRACKET_CW, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			head();
			setState(31);
			match(BRACKET_OW);
			setState(33); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(32);
				statement();
				}
				}
				setState(35); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 6146L) != 0) );
			setState(37);
			match(BRACKET_CW);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HeadContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(par.IDENTIFIER, 0); }
		public TerminalNode BRACKET_OR() { return getToken(par.BRACKET_OR, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public TerminalNode BRACKET_CR() { return getToken(par.BRACKET_CR, 0); }
		public Type_parametersContext type_parameters() {
			return getRuleContext(Type_parametersContext.class,0);
		}
		public HeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_head; }
	}

	public final HeadContext head() throws RecognitionException {
		HeadContext _localctx = new HeadContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_head);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			type();
			setState(40);
			match(IDENTIFIER);
			setState(42);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BRACKET_OS) {
				{
				setState(41);
				type_parameters();
				}
			}

			setState(44);
			match(BRACKET_OR);
			setState(45);
			args();
			setState(46);
			match(BRACKET_CR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type_parametersContext extends ParserRuleContext {
		public TerminalNode BRACKET_OS() { return getToken(par.BRACKET_OS, 0); }
		public Type_paramsContext type_params() {
			return getRuleContext(Type_paramsContext.class,0);
		}
		public TerminalNode BRACKET_CS() { return getToken(par.BRACKET_CS, 0); }
		public Type_parametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_parameters; }
	}

	public final Type_parametersContext type_parameters() throws RecognitionException {
		Type_parametersContext _localctx = new Type_parametersContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_type_parameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(BRACKET_OS);
			setState(49);
			type_params();
			setState(50);
			match(BRACKET_CS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type_paramsContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(par.COMMA, 0); }
		public Type_paramsContext type_params() {
			return getRuleContext(Type_paramsContext.class,0);
		}
		public Type_paramsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_params; }
	}

	public final Type_paramsContext type_params() throws RecognitionException {
		Type_paramsContext _localctx = new Type_paramsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_type_params);
		try {
			setState(57);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				type();
				setState(54);
				match(COMMA);
				setState(55);
				type_params();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgsContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(par.IDENTIFIER, 0); }
		public TerminalNode COMMA() { return getToken(par.COMMA, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_args);
		try {
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(59);
				type();
				setState(60);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(62);
				type();
				setState(63);
				match(IDENTIFIER);
				setState(64);
				match(COMMA);
				setState(65);
				args();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public Return_sContext return_s() {
			return getRuleContext(Return_sContext.class,0);
		}
		public Assign_sContext assign_s() {
			return getRuleContext(Assign_sContext.class,0);
		}
		public Init_sContext init_s() {
			return getRuleContext(Init_sContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		try {
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				return_s();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				assign_s();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(71);
				init_s();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_sContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(par.RETURN, 0); }
		public TerminalNode IDENTIFIER() { return getToken(par.IDENTIFIER, 0); }
		public TerminalNode SEMICOLON() { return getToken(par.SEMICOLON, 0); }
		public Return_sContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_s; }
	}

	public final Return_sContext return_s() throws RecognitionException {
		Return_sContext _localctx = new Return_sContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_return_s);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(RETURN);
			setState(75);
			match(IDENTIFIER);
			setState(76);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_sContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(par.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(par.IDENTIFIER, i);
		}
		public TerminalNode EQUAL() { return getToken(par.EQUAL, 0); }
		public TerminalNode SEMICOLON() { return getToken(par.SEMICOLON, 0); }
		public Assign_sContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_s; }
	}

	public final Assign_sContext assign_s() throws RecognitionException {
		Assign_sContext _localctx = new Assign_sContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_assign_s);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(IDENTIFIER);
			setState(79);
			match(EQUAL);
			setState(80);
			match(IDENTIFIER);
			setState(81);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Init_sContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(par.IDENTIFIER, 0); }
		public TerminalNode SEMICOLON() { return getToken(par.SEMICOLON, 0); }
		public Init_sContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init_s; }
	}

	public final Init_sContext init_s() throws RecognitionException {
		Init_sContext _localctx = new Init_sContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_init_s);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			type();
			setState(84);
			match(IDENTIFIER);
			setState(85);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode TYPE_IDENTIFIER() { return getToken(par.TYPE_IDENTIFIER, 0); }
		public TerminalNode IDENTIFIER() { return getToken(par.IDENTIFIER, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_la = _input.LA(1);
			if ( !(_la==IDENTIFIER || _la==TYPE_IDENTIFIER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\rZ\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0005\u0000\u0018"+
		"\b\u0000\n\u0000\f\u0000\u001b\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0004\u0001\"\b\u0001\u000b\u0001\f\u0001#\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002+\b"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004:\b\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005D\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006I\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0000\u0000\u000b\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0000\u0001\u0001\u0000\u000b\fU\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0002\u001e\u0001\u0000\u0000\u0000\u0004\'\u0001\u0000\u0000\u0000\u0006"+
		"0\u0001\u0000\u0000\u0000\b9\u0001\u0000\u0000\u0000\nC\u0001\u0000\u0000"+
		"\u0000\fH\u0001\u0000\u0000\u0000\u000eJ\u0001\u0000\u0000\u0000\u0010"+
		"N\u0001\u0000\u0000\u0000\u0012S\u0001\u0000\u0000\u0000\u0014W\u0001"+
		"\u0000\u0000\u0000\u0016\u0018\u0003\u0002\u0001\u0000\u0017\u0016\u0001"+
		"\u0000\u0000\u0000\u0018\u001b\u0001\u0000\u0000\u0000\u0019\u0017\u0001"+
		"\u0000\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a\u001c\u0001"+
		"\u0000\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000\u001c\u001d\u0005"+
		"\u0000\u0000\u0001\u001d\u0001\u0001\u0000\u0000\u0000\u001e\u001f\u0003"+
		"\u0004\u0002\u0000\u001f!\u0005\u0007\u0000\u0000 \"\u0003\f\u0006\u0000"+
		"! \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000\u0000#!\u0001\u0000\u0000"+
		"\u0000#$\u0001\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%&\u0005\b\u0000"+
		"\u0000&\u0003\u0001\u0000\u0000\u0000\'(\u0003\u0014\n\u0000(*\u0005\u000b"+
		"\u0000\u0000)+\u0003\u0006\u0003\u0000*)\u0001\u0000\u0000\u0000*+\u0001"+
		"\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,-\u0005\u0003\u0000\u0000"+
		"-.\u0003\n\u0005\u0000./\u0005\u0004\u0000\u0000/\u0005\u0001\u0000\u0000"+
		"\u000001\u0005\u0005\u0000\u000012\u0003\b\u0004\u000023\u0005\u0006\u0000"+
		"\u00003\u0007\u0001\u0000\u0000\u00004:\u0003\u0014\n\u000056\u0003\u0014"+
		"\n\u000067\u0005\t\u0000\u000078\u0003\b\u0004\u00008:\u0001\u0000\u0000"+
		"\u000094\u0001\u0000\u0000\u000095\u0001\u0000\u0000\u0000:\t\u0001\u0000"+
		"\u0000\u0000;<\u0003\u0014\n\u0000<=\u0005\u000b\u0000\u0000=D\u0001\u0000"+
		"\u0000\u0000>?\u0003\u0014\n\u0000?@\u0005\u000b\u0000\u0000@A\u0005\t"+
		"\u0000\u0000AB\u0003\n\u0005\u0000BD\u0001\u0000\u0000\u0000C;\u0001\u0000"+
		"\u0000\u0000C>\u0001\u0000\u0000\u0000D\u000b\u0001\u0000\u0000\u0000"+
		"EI\u0003\u000e\u0007\u0000FI\u0003\u0010\b\u0000GI\u0003\u0012\t\u0000"+
		"HE\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HG\u0001\u0000\u0000"+
		"\u0000I\r\u0001\u0000\u0000\u0000JK\u0005\u0001\u0000\u0000KL\u0005\u000b"+
		"\u0000\u0000LM\u0005\u0002\u0000\u0000M\u000f\u0001\u0000\u0000\u0000"+
		"NO\u0005\u000b\u0000\u0000OP\u0005\n\u0000\u0000PQ\u0005\u000b\u0000\u0000"+
		"QR\u0005\u0002\u0000\u0000R\u0011\u0001\u0000\u0000\u0000ST\u0003\u0014"+
		"\n\u0000TU\u0005\u000b\u0000\u0000UV\u0005\u0002\u0000\u0000V\u0013\u0001"+
		"\u0000\u0000\u0000WX\u0007\u0000\u0000\u0000X\u0015\u0001\u0000\u0000"+
		"\u0000\u0006\u0019#*9CH";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}